"""
Agent Supervisor CLI
Unified coordinator providing safety validation, code necessity auditing,
and iterative self-annealing execution loops.
"""

import argparse
from pathlib import Path
import sys
from typing import List

# Ensure project root is in sys.path so execution package can be imported directly
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from execution.guardian import SafetyGuardian
from execution.code_auditor import CodeAuditor
from execution.loop_runner import LoopRunner


class AgentSupervisor:
    """
    Coordinates workspace safety guards, code necessity analysis,
    and iterative loop execution.
    """

    def __init__(self, root_dir: Path):
        self.root_dir = root_dir.resolve()
        self.guardian = SafetyGuardian(self.root_dir)
        self.auditor = CodeAuditor()
        self.runner = LoopRunner(self.root_dir)

    """
    Runs safety check to ensure critical files were not deleted or modified.
    """
    def check_safety(self) -> int:
        violations = self.guardian.verify_integrity()
        if violations:
            print("\n[SAFETY ALERT] Critical asset violations detected:")
            for v in violations:
                print(f"  - {v}")
            return 1
        print("[SAFETY OK] All protected files and directives are intact.")
        return 0

    """
    Audits python files for line necessity, conciseness, and dead code.
    """
    def audit_code(self, target_path: Path) -> int:
        print(f"\n[AUDITING CODE] Checking: {target_path}")
        files_to_check: List[Path] = []
        if target_path.is_file():
            files_to_check.append(target_path)
        else:
            for ext in ("*.py",):
                files_to_check.extend(target_path.rglob(ext))

        total_findings = 0
        for f in files_to_check:
            if ".tmp" in f.parts or "__pycache__" in f.parts:
                continue
            findings = self.auditor.audit_file(f)
            if findings:
                print(f"\n--- {f.relative_to(self.root_dir)} ({len(findings)} findings) ---")
                for item in findings:
                    total_findings += 1
                    print(
                        f"  L{item.line} [{item.rule}]: {item.message}\n"
                        f"    Suggestion: {item.suggestion}"
                    )

        if total_findings == 0:
            print("[AUDIT PASSED] All lines are necessary, concise, and within bounds.")
            return 0
        print(f"\n[AUDIT COMPLETED] Found {total_findings} potential optimizations/issues.")
        return 1 if total_findings > 0 else 0

    """
    Runs program in an automated loop until verified output is achieved.
    """
    def run_loop(
        self, command: List[str], expected_files: List[str], max_iter: int = 5
    ) -> int:
        print(f"\n[LOOP RUNNER] Executing: {' '.join(command)}")
        print(f"Expected deliverables: {expected_files}")
        self.runner.max_iterations = max_iter
        result = self.runner.run_until_verified(command, expected_files)

        if result.verified:
            print(f"\n[SUCCESS] Verified output achieved on iteration {result.iteration}!")
            print(f"Stdout:\n{result.stdout.strip()}")
            return 0

        print(f"\n[FAILED] Loop finished without achieving verified output.")
        print(f"Exit code: {result.return_code}")
        if result.error_summary:
            print(f"Diagnostic error: {result.error_summary}")
        if result.missing_outputs:
            print(f"Missing required deliverables: {result.missing_outputs}")
        return 1


"""
Main CLI entrypoint.
"""
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Autonomous Agent Supervisor & Quality Guardian"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Safety command
    subparsers.add_parser("safety", help="Check workspace integrity")
    subparsers.add_parser("snapshot", help="Capture workspace snapshot")

    # Audit command
    audit_parser = subparsers.add_parser("audit", help="Audit code necessity")
    audit_parser.add_argument(
        "--path", default="execution", help="Path to audit (file or dir)"
    )

    # Loop command
    loop_parser = subparsers.add_parser("loop", help="Run program in a self-healing loop")
    loop_parser.add_argument(
        "--expect", nargs="*", default=[], help="Expected output files"
    )
    loop_parser.add_argument(
        "--max-iter", type=int, default=5, help="Maximum iterations"
    )
    loop_parser.add_argument("cmd", nargs=argparse.REMAINDER, help="Command to run")

    args = parser.parse_args()
    root = Path.cwd()
    supervisor = AgentSupervisor(root)

    if args.command == "safety":
        sys.exit(supervisor.check_safety())
    elif args.command == "snapshot":
        supervisor.guardian.capture_snapshot()
        print("[SNAPSHOT] Workspace safety snapshot captured successfully.")
        sys.exit(0)
    elif args.command == "audit":
        target = (root / args.path).resolve()
        sys.exit(supervisor.audit_code(target))
    elif args.command == "loop":
        cmd = args.cmd[1:] if args.cmd and args.cmd[0] == "--" else args.cmd
        if not cmd:
            print("[ERROR] No command specified to run in loop.")
            sys.exit(1)
        sys.exit(supervisor.run_loop(cmd, args.expect, args.max_iter))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
