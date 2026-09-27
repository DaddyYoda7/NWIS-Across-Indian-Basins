# Directive: Autonomous Agent Supervisor & Self-Annealing Loop

## 1. Objective
Ensure zero hallucinations, prevent destructive modifications or deletions of critical assets, audit every line of written code for necessity and conciseness, and execute programs in an automated self-annealing loop until verified optimal output is achieved.

## 2. Protected Assets & Safety Boundaries
The following files and patterns are strictly protected by `execution/guardian.py`:
- `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`
- `directives/` (all SOPs)
- `.env`, `credentials.json`, `token.json`
- Source files cannot be deleted without explicit confirmation or safe archiving.

## 3. Code Necessity & Conciseness Audit Protocol
Before any code is considered final, `execution/code_auditor.py` checks:
1. **Unused Imports and Variables**: Flags unused symbols using AST inspection.
2. **Line Bloat & Redundancy**: Identifies redundant assignments, verbose single-use variables, trivial wrapper functions, and unnecessarily complex branching.
3. **File Size Limits**: Warns and fails if files exceed 250-300 lines.
4. **Necessity Assessment**: Every block of code must serve an explicit purpose in the pipeline; phantom logic or hallucinated boilerplate is flagged for elimination.

## 4. Autonomous Self-Annealing Loop Protocol
When executing a script via `execution/loop_runner.py`:
1. **Execution**: Run deterministic command/script with isolated timeout and output capture.
2. **Verification Check**:
   - Exit code must be 0.
   - Required output deliverables must be generated, non-empty, and valid.
   - Assertions or validation tests must pass.
3. **Failure Diagnosis**:
   - Parse traceback, identify exact file and line number, categorize error (Syntax, Import, Runtime, FileNotFoundError, etc.).
   - Log diagnostic report to `.tmp/loop_history.json`.
4. **Anneal & Loop**:
   - Apply fixes and re-execute iteratively until target output passes all verification checks or max iterations is reached.

## 5. Deliverables & State Tracking
- Diagnostics log: `.tmp/loop_history.json`
- State snapshots: `.tmp/safety_snapshot.json`
- Execution logs: `.tmp/supervisor_audit.log`
