"""
Autonomous Self-Annealing Loop Runner
Executes scripts/tests in an iterative loop, captures outputs, diagnoses errors,
verifies required deliverables, and tracks iteration history.
"""

from dataclasses import dataclass, asdict
import json
from pathlib import Path
import subprocess
import time
from typing import List, Optional


@dataclass
class IterationResult:
    iteration: int
    command: List[str]
    return_code: int
    duration_sec: float
    stdout: str
    stderr: str
    error_summary: Optional[str]
    missing_outputs: List[str]
    verified: bool


class LoopRunner:
    """
    Runs programs repeatedly in a self-annealing loop until verified
    success is achieved or maximum iterations are exhausted.
    """

    def __init__(self, root_dir: Optional[Path] = None, max_iterations: int = 5):
        self.root_dir = (root_dir or Path.cwd()).resolve()
        self.max_iterations = max_iterations
        self.history_file = self.root_dir / ".tmp" / "loop_history.json"

    """
    Executes a single iteration of the command and captures execution metrics.
    """
    def _execute_once(
        self, cmd: List[str], timeout: int
    ) -> tuple[int, str, str, float]:
        start = time.time()
        try:
            res = subprocess.run(
                cmd,
                cwd=str(self.root_dir),
                capture_output=True,
                text=True,
                timeout=timeout,
            )
            duration = round(time.time() - start, 3)
            return res.returncode, res.stdout, res.stderr, duration
        except subprocess.TimeoutExpired as e:
            duration = round(time.time() - start, 3)
            return -1, "", f"Execution timed out after {timeout} seconds.", duration
        except Exception as e:
            duration = round(time.time() - start, 3)
            return -1, "", str(e), duration

    """
    Extracts high-level error summary and line diagnostics from stderr.
    """
    def _diagnose_error(self, stderr: str) -> Optional[str]:
        if not stderr:
            return None
        lines = [line.strip() for line in stderr.splitlines() if line.strip()]
        if not lines:
            return None

        # Look for last traceback line with exception
        for line in reversed(lines):
            if any(err in line for err in ["Error", "Exception", "Timeout"]):
                return line
        return lines[-1]

    """
    Verifies that all expected deliverables exist and are non-empty.
    """
    def _verify_deliverables(self, expected_files: List[str]) -> List[str]:
        missing: List[str] = []
        for f in expected_files:
            p = self.root_dir / f
            if not p.exists() or p.stat().st_size == 0:
                missing.append(f)
        return missing

    """
    Runs target program in a loop until required verified output is achieved.
    """
    def run_until_verified(
        self,
        command: List[str],
        expected_outputs: Optional[List[str]] = None,
        timeout_sec: int = 60,
    ) -> IterationResult:
        expected = expected_outputs or []
        history: List[dict] = []
        self.history_file.parent.mkdir(parents=True, exist_ok=True)

        last_result: Optional[IterationResult] = None

        for iteration in range(1, self.max_iterations + 1):
            ret_code, stdout, stderr, duration = self._execute_once(
                command, timeout=timeout_sec
            )
            err_summary = self._diagnose_error(stderr)
            missing = self._verify_deliverables(expected)

            verified = (ret_code == 0) and (len(missing) == 0)

            last_result = IterationResult(
                iteration=iteration,
                command=command,
                return_code=ret_code,
                duration_sec=duration,
                stdout=stdout,
                stderr=stderr,
                error_summary=err_summary,
                missing_outputs=missing,
                verified=verified,
            )

            history.append(asdict(last_result))
            with open(self.history_file, "w", encoding="utf-8") as f:
                json.dump(history, f, indent=2)

            if verified:
                break

        return last_result
