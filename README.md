# Test Execution Skill

> Test operations for AI agents — run unit/integration/E2E tests, track coverage deltas, debug failures, and gate merges on quality via mcp-test-runner.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--test--runner-green)](https://github.com/zavora-ai/mcp-test-runner)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Pre-Merge Validation | 3 | Unit + coverage + integration |
| Debug Failure | 2 | Identify test + root cause |
| Targeted Tests | 1 | Run specific file/pattern |

### Without this skill:
- Tests skipped "to save time"
- Coverage decreases go unnoticed
- Flaky tests rerun endlessly without investigation
- No coverage delta reporting (just absolute numbers)

### With this skill:
- Tests always run before merge approval
- Coverage delta tracked (regression = blocked)
- Flaky vs genuine failures distinguished
- Clear failure reports with stack traces

## Installation

```bash
git clone https://github.com/zavora-ai/skill-test-execution.git \
  ~/.skills/skills/test-execution
```

## Requirements

**Required:** `mcp-test-runner` (7 tools)

**Cross-MCP:**
- `mcp-github` — approve PRs only when tests pass
- `mcp-cicd` — post-deploy verification
- `mcp-jira` — create bugs from test failures

## Folder Structure

```
test-execution/
├── SKILL.md                       # Decision tree + test strategy
├── scripts/
│   └── coverage_delta.py          # Coverage regression detector
├── references/
│   ├── tool-sequences.md          # 7 tools
│   ├── cross-mcp-workflows.md     # Tests + GitHub + CI/CD + Jira
│   └── examples.md                # Run, debug, coverage
├── README.md
└── LICENSE
```

## Scripts

### `coverage_delta.py`
```bash
python scripts/coverage_delta.py '{"current": {"line": 82}, "baseline": {"line": 80}}'
# → {"line_delta": 2.0, "regression": false, "message": "✅ Coverage improved by +2.0%"}
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Pre-merge gate | Tests always run before approval |
| Coverage tracking | Delta reported, regressions blocked |
| Flaky detection | Distinguish flaky from genuine failures |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
