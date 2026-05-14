#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-127.0.0.1}"
OUTPUT="${2:-reports/nmap-local.xml}"

python3 scripts/validate_target.py "$TARGET"
mkdir -p "$(dirname "$OUTPUT")"

if command -v docker >/dev/null 2>&1; then
  docker run --rm --network host instrumentisto/nmap -sV -oX - "$TARGET" > "$OUTPUT"
elif command -v nmap >/dev/null 2>&1; then
  nmap -sV -oX "$OUTPUT" "$TARGET"
else
  echo "Neither docker nor nmap is available." >&2
  echo "Install Docker or Nmap, then rerun this command." >&2
  exit 127
fi

echo "Wrote $OUTPUT"
