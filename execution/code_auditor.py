"""
Code Auditor Module
Performs AST-level static analysis to assess code necessity, line-count limits,
redundant logic, unused symbols, and opportunities for simplification.
"""

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import List, Set


@dataclass
class Finding:
    file: str
    line: int
    rule: str
    message: str
    suggestion: str


class CodeAuditor:
    """
    Audits Python source files to ensure every line is necessary,
    concise, and compliant with file size limits.
    """

    MAX_FILE_LINES = 300
    MAX_FUNC_LINES = 60

    """
    Runs all audit checks across the provided file.
    """
    def audit_file(self, file_path: Path) -> List[Finding]:
        findings: List[Finding] = []
        if not file_path.exists() or file_path.suffix != ".py":
            return findings

        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        lines = code.splitlines()
        self._check_file_length(file_path, lines, findings)

        try:
            tree = ast.parse(code, filename=str(file_path))
        except SyntaxError as e:
            findings.append(Finding(
                file=file_path.name,
                line=e.lineno or 1,
                rule="SYNTAX_ERROR",
                message=f"Syntax error: {e.msg}",
                suggestion="Fix syntax error before auditing."
            ))
            return findings

        self._check_ast_nodes(file_path, tree, findings)
        self._check_unused_imports(file_path, tree, findings)
        return findings

    """
    Checks whether file or individual functions exceed size constraints.
    """
    def _check_file_length(
        self, file_path: Path, lines: List[str], findings: List[Finding]
    ) -> None:
        total_lines = len(lines)
        if total_lines > self.MAX_FILE_LINES:
            findings.append(Finding(
                file=file_path.name,
                line=1,
                rule="FILE_TOO_LONG",
                message=f"File has {total_lines} lines (max {self.MAX_FILE_LINES}).",
                suggestion="Split by responsibility or extract sub-components."
            ))

    """
    Traverses AST to identify redundancy, unnecessary lines, and dead code.
    """
    def _check_ast_nodes(
        self, file_path: Path, tree: ast.AST, findings: List[Finding]
    ) -> None:
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                length = (node.end_lineno or node.lineno) - node.lineno
                if length > self.MAX_FUNC_LINES:
                    findings.append(Finding(
                        file=file_path.name,
                        line=node.lineno,
                        rule="FUNCTION_TOO_LONG",
                        message=f"Function '{node.name}' has {length} lines.",
                        suggestion="Extract helper methods to simplify."
                    ))

            if isinstance(node, ast.If):
                self._check_redundant_bool_compare(file_path, node, findings)
                self._check_boolean_return(file_path, node, findings)

            if hasattr(node, "body") and isinstance(node.body, list):
                self._check_single_use_return(file_path, node.body, findings)
            if hasattr(node, "orelse") and isinstance(node.orelse, list):
                self._check_single_use_return(file_path, node.orelse, findings)

            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                self._check_unreachable_code(file_path, node, findings)

    """
    Flags redundant comparisons to boolean literals like 'if x == True:'.
    """
    def _check_redundant_bool_compare(
        self, file_path: Path, node: ast.If, findings: List[Finding]
    ) -> None:
        if isinstance(node.test, ast.Compare):
            for comparator in node.test.comparators:
                if isinstance(comparator, ast.Constant) and isinstance(comparator.value, bool):
                    findings.append(Finding(
                        file=file_path.name,
                        line=node.lineno,
                        rule="REDUNDANT_BOOL_COMPARE",
                        message="Comparing explicitly to True/False literal.",
                        suggestion="Use 'if cond:' or 'if not cond:' directly."
                    ))

    """
    Flags verbose if/else returning True/False that can be one line.
    """
    def _check_boolean_return(
        self, file_path: Path, node: ast.If, findings: List[Finding]
    ) -> None:
        if (
            len(node.body) == 1
            and isinstance(node.body[0], ast.Return)
            and isinstance(node.body[0].value, ast.Constant)
            and isinstance(node.body[0].value.value, bool)
            and len(node.orelse) == 1
            and isinstance(node.orelse[0], ast.Return)
            and isinstance(node.orelse[0].value, ast.Constant)
            and isinstance(node.orelse[0].value.value, bool)
        ):
            findings.append(Finding(
                file=file_path.name,
                line=node.lineno,
                rule="SIMPLIFY_BOOLEAN_RETURN",
                message="Verbous if/else returning booleans.",
                suggestion="Replace with concise 'return bool(condition)'."
            ))

    """
    Flags redundant assignment right before return in any block (e.g. res = x; return res).
    """
    def _check_single_use_return(
        self, file_path: Path, block: list, findings: List[Finding]
    ) -> None:
        if len(block) < 2:
            return
        last, second_last = block[-1], block[-2]
        if (
            isinstance(last, ast.Return)
            and isinstance(last.value, ast.Name)
            and isinstance(second_last, ast.Assign)
            and len(second_last.targets) == 1
            and isinstance(second_last.targets[0], ast.Name)
            and last.value.id == second_last.targets[0].id
        ):
            findings.append(Finding(
                file=file_path.name,
                line=second_last.lineno,
                rule="REDUNDANT_INTERMEDIATE_VAR",
                message=f"Variable '{last.value.id}' assigned and immediately returned.",
                suggestion="Inline expression directly into return statement."
            ))

    """
    Detects unreachable statements following return or raise.
    """
    def _check_unreachable_code(
        self, file_path: Path, node: ast.FunctionDef, findings: List[Finding]
    ) -> None:
        terminal_seen = False
        for stmt in node.body:
            if terminal_seen:
                findings.append(Finding(
                    file=file_path.name,
                    line=stmt.lineno,
                    rule="UNREACHABLE_CODE",
                    message="Statement appears after terminal return or raise.",
                    suggestion="Remove dead/unreachable code."
                ))
                break
            if isinstance(stmt, (ast.Return, ast.Raise)):
                terminal_seen = True

    """
    Identifies imported names that are never referenced in the module.
    """
    def _check_unused_imports(
        self, file_path: Path, tree: ast.AST, findings: List[Finding]
    ) -> None:
        imported_names: dict[str, int] = {}
        used_names: Set[str] = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.asname or alias.name
                    imported_names[name] = node.lineno
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    name = alias.asname or alias.name
                    imported_names[name] = node.lineno
            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                used_names.add(node.id)

        for name, lineno in imported_names.items():
            base_name = name.split(".")[0]
            if name not in used_names and base_name not in used_names and name != "__all__":
                findings.append(Finding(
                    file=file_path.name,
                    line=lineno,
                    rule="UNUSED_IMPORT",
                    message=f"Imported '{name}' is never used.",
                    suggestion="Remove unnecessary import line to keep code concise."
                ))
