"""
Safety Guardian Module
Monitors workspace integrity, prevents accidental deletion of critical files,
and validates workspace state against safety snapshots.
"""

from dataclasses import dataclass, asdict
import hashlib
import json
from pathlib import Path
from typing import Dict, List, Optional

PROTECTED_EXACT_FILES = {
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".gitignore",
    ".env",
    "credentials.json",
    "token.json",
}

PROTECTED_DIRECTORIES = {
    "directives",
}


@dataclass
class FileState:
    path: str
    size: int
    sha256: str
    is_protected: bool


class SafetyGuardian:
    """
    Guards workspace against unauthorized or destructive deletions.
    Provides snapshot and integrity verification mechanisms.
    """

    def __init__(self, root_dir: Optional[Path] = None):
        self.root_dir = (root_dir or Path.cwd()).resolve()
        self.snapshot_file = self.root_dir / ".tmp" / "safety_snapshot.json"

    """
    Determines if a given relative or absolute path is protected.
    """
    def is_protected(self, target_path: Path) -> bool:
        try:
            rel = target_path.resolve().relative_to(self.root_dir)
        except ValueError:
            return True

        rel_str = rel.as_posix()
        parts = rel.parts

        if not parts:
            return True

        if parts[0] in PROTECTED_DIRECTORIES:
            return True

        if rel_str in PROTECTED_EXACT_FILES:
            return True

        return False

    """
    Computes SHA-256 hash of a file for integrity tracking.
    """
    def compute_sha256(self, file_path: Path) -> str:
        hasher = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    """
    Captures snapshot of current workspace files and saves to .tmp.
    """
    def capture_snapshot(self) -> Dict[str, dict]:
        snapshot: Dict[str, dict] = {}
        for p in self.root_dir.rglob("*"):
            if not p.is_file():
                continue
            if ".tmp" in p.parts or "__pycache__" in p.parts:
                continue

            rel_str = p.relative_to(self.root_dir).as_posix()
            try:
                sha = self.compute_sha256(p)
                state = FileState(
                    path=rel_str,
                    size=p.stat().st_size,
                    sha256=sha,
                    is_protected=self.is_protected(p),
                )
                snapshot[rel_str] = asdict(state)
            except (PermissionError, FileNotFoundError):
                continue

        self.snapshot_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.snapshot_file, "w", encoding="utf-8") as f:
            json.dump(snapshot, f, indent=2)

        return snapshot

    """
    Validates current workspace against previous snapshot.
    Returns list of critical violations (e.g. deleted protected files).
    """
    def verify_integrity(self) -> List[str]:
        violations: List[str] = []
        if not self.snapshot_file.exists():
            self.capture_snapshot()
            return violations

        with open(self.snapshot_file, "r", encoding="utf-8") as f:
            prev_snapshot = json.load(f)

        for rel_path, data in prev_snapshot.items():
            file_path = self.root_dir / rel_path
            if not file_path.exists():
                if data.get("is_protected", False):
                    violations.append(
                        f"CRITICAL: Protected file was deleted: {rel_path}"
                    )
                else:
                    violations.append(f"WARNING: File was deleted: {rel_path}")

        return violations

    """
    Pre-flight guard check before deleting a file.
    Raises PermissionError if target is protected.
    """
    def assert_can_delete(self, target_path: Path) -> None:
        target = target_path.resolve()
        if self.is_protected(target):
            raise PermissionError(
                f"SAFETY VIOLATION: Cannot delete protected asset: {target}"
            )
