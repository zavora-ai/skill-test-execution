# Test Runner Tool Sequences

## Tools (7)
| Tool | Purpose |
|------|---------|
| `run_unit_tests` | Fast unit tests (< 2 min) |
| `run_integration_tests` | Service integration tests |
| `run_e2e_tests` | Browser/E2E tests |
| `run_specific_tests` | Run by file/name pattern |
| `get_results` | Pass/fail/skip counts |
| `get_coverage` | Line/branch coverage % |
| `get_test_logs` | Failure details + stack traces |

## Sequence: Pre-Merge Validation (3 calls)
```
1. run_unit_tests() → {passed: 142, failed: 0, skipped: 3, duration: "45s"}
2. get_coverage() → {line: 82%, branch: 74%, delta: "+1.2%"}
3. run_integration_tests() → {passed: 28, failed: 0, duration: "3m 12s"}
→ All green, coverage increased. Safe to merge.
```

## Sequence: Debug Failure (2 calls)
```
1. get_results(run_id: "latest") → {failed: ["test_payment_retry", "test_webhook_timeout"]}
2. get_test_logs(run_id: "latest", test: "test_payment_retry")
   → "assertion failed at src/retry.rs:45: expected 3 retries, got 0"
```
