# Test Execution Cross-MCP Workflows

## Tests + GitHub: Pre-Merge Gate
```
TESTS: run_unit_tests() → {passed: 142, failed: 0}
TESTS: get_coverage() → {line: 82%, delta: "+1.2%"}
GITHUB: create_review(number: 42, event: "APPROVE", body: "✅ Tests pass. Coverage +1.2%.")
```

## Tests + CI/CD: Post-Deploy Verification
```
CICD: trigger_deployment(env: "staging")
TESTS: run_integration_tests(env: "staging") → {passed: 28, failed: 0}
TESTS: run_e2e_tests(env: "staging") → {passed: 12, failed: 0}
SLACK: send_message(channel: "#deploys", text: "✅ Staging verified: 28 integration + 12 E2E tests pass")
```

## Tests + Jira: Failure → Bug
```
TESTS: get_results(run_id: "latest") → {failed: ["test_payment_retry"]}
TESTS: get_test_logs(test: "test_payment_retry") → "expected 3 retries, got 0"
JIRA: create_issue(type: "Bug", summary: "fix: payment retry not executing", description: "Test: test_payment_retry\nError: expected 3 retries, got 0")
```
