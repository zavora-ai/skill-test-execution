# Test Execution Examples

## Example 1: "Run the tests"
```
run_unit_tests() → {passed: 142, failed: 0, duration: "45s"}
get_coverage() → {line: 82%, branch: 74%}
```
Response: "✅ All 142 tests pass. Coverage: 82% lines, 74% branches (+1.2% vs main)."

## Example 2: "Why are tests failing?"
```
get_results(run_id: "latest") → {failed: ["test_payment_retry"]}
get_test_logs(test: "test_payment_retry") → "expected 3 retries, got 0"
```
Response: "❌ test_payment_retry failing: retry logic not executing. Check retry config."

## Example 3: "Just run the auth tests"
```
run_specific_tests(pattern: "src/auth/*_test.rs") → {passed: 8, failed: 0}
```
Response: "✅ 8 auth tests pass."
