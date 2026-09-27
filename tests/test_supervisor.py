"""
Unit and Integration Tests for Agent Supervisor System
Tests SafetyGuardian, CodeAuditor, LoopRunner, and AgentSupervisor orchestration.
"""

from pathlib import Path
import tempfile
import unittest

from execution.guardian import SafetyGuardian
from execution.code_auditor import CodeAuditor
from execution.loop_runner import LoopRunner
from execution.agent_supervisor import AgentSupervisor


class TestSafetyGuardian(unittest.TestCase):
    """
    Tests workspace safety guard and protected asset detection.
    """

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "directives").mkdir(parents=True)
        (self.root / "directives" / "sop.md").write_text("SOP test", encoding="utf-8")
        (self.root / "AGENTS.md").write_text("Agents doc", encoding="utf-8")
        (self.root / "scratch.txt").write_text("Scratch", encoding="utf-8")
        self.guardian = SafetyGuardian(self.root)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_protected_identification(self):
        self.assertTrue(self.guardian.is_protected(self.root / "AGENTS.md"))
        self.assertTrue(self.guardian.is_protected(self.root / "directives" / "sop.md"))
        self.assertFalse(self.guardian.is_protected(self.root / "scratch.txt"))

    def test_snapshot_and_integrity_check(self):
        self.guardian.capture_snapshot()
        self.assertEqual(len(self.guardian.verify_integrity()), 0)

        # Deleting a protected file must trigger a critical violation
        (self.root / "AGENTS.md").unlink()
        violations = self.guardian.verify_integrity()
        self.assertTrue(any("CRITICAL" in v and "AGENTS.md" in v for v in violations))


class TestCodeAuditor(unittest.TestCase):
    """
    Tests AST-level code necessity and conciseness rules.
    """

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.auditor = CodeAuditor()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_detect_unused_import_and_redundancy(self):
        sample_code = """import os
import sys

def check_value(x):
    if x == True:
        res = 42
        return res
    return 0
"""
        test_file = self.root / "sample.py"
        test_file.write_text(sample_code, encoding="utf-8")

        findings = self.auditor.audit_file(test_file)
        rules = [f.rule for f in findings]

        self.assertIn("UNUSED_IMPORT", rules)
        self.assertIn("REDUNDANT_BOOL_COMPARE", rules)
        self.assertIn("REDUNDANT_INTERMEDIATE_VAR", rules)

    def test_clean_concise_code_has_no_findings(self):
        clean_code = '''"""Clean module."""

def add_numbers(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b
'''
        test_file = self.root / "clean.py"
        test_file.write_text(clean_code, encoding="utf-8")
        findings = self.auditor.audit_file(test_file)
        self.assertEqual(len(findings), 0)


class TestLoopRunner(unittest.TestCase):
    """
    Tests automated self-annealing execution loop.
    """

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.runner = LoopRunner(self.root, max_iterations=3)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_loop_success_with_deliverable(self):
        out_file = self.root / "output.txt"
        cmd = [
            "python",
            "-c",
            f"from pathlib import Path; Path('{out_file.as_posix()}').write_text('DONE', encoding='utf-8')",
        ]
        result = self.runner.run_until_verified(cmd, ["output.txt"])
        self.assertTrue(result.verified)
        self.assertEqual(result.return_code, 0)
        self.assertTrue(out_file.exists())


class TestAgentSupervisor(unittest.TestCase):
    """
    Tests unified AgentSupervisor CLI coordinator.
    """

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "execution").mkdir(parents=True)
        (self.root / "execution" / "sample.py").write_text("x = 1\n", encoding="utf-8")
        self.supervisor = AgentSupervisor(self.root)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_supervisor_safety_and_audit(self):
        self.supervisor.guardian.capture_snapshot()
        self.assertEqual(self.supervisor.check_safety(), 0)
        self.assertEqual(self.supervisor.audit_code(self.root / "execution"), 0)


if __name__ == "__main__":
    unittest.main()
