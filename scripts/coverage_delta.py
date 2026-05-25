#!/usr/bin/env python3
"""Calculate coverage delta and flag regressions."""
import json, sys

def analyze(data):
    current = data.get("current", {})
    baseline = data.get("baseline", {})
    
    result = {
        "line_coverage": current.get("line", 0),
        "branch_coverage": current.get("branch", 0),
        "line_delta": round(current.get("line", 0) - baseline.get("line", 0), 2),
        "branch_delta": round(current.get("branch", 0) - baseline.get("branch", 0), 2),
        "regression": False,
        "message": "",
    }
    if result["line_delta"] < -1:
        result["regression"] = True
        result["message"] = f"⚠️ Coverage decreased by {abs(result['line_delta'])}%. Add tests before merging."
    elif result["line_delta"] > 0:
        result["message"] = f"✅ Coverage improved by +{result['line_delta']}%"
    else:
        result["message"] = "→ Coverage unchanged"
    return result

if __name__ == "__main__":
    print(json.dumps(analyze(json.loads(sys.argv[1])), indent=2))
