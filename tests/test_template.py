from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "Makefile",
    "mock/mock_service.py",
    "scripts/validate_target.py",
    "scripts/run_scan.sh",
    "benchmark/task.md",
    "benchmark/expected_output.json",
]
for rel in required:
    assert (root / rel).exists(), f"missing {rel}"

expected = json.loads((root / "benchmark/expected_output.json").read_text())
assert expected["task"] == "nmap_local_scan"
assert "127.0.0.1" in expected["allowed_targets"]
print("nmap_template validation passed")
