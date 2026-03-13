#!/bin/bash
set -euo pipefail

echo "Preparing $1 for submission"

typst compile "$1/lab_report.typ" "$1.pdf"
git ls-files | grep "^$1" | xargs zip -r "$1"

echo "Finished"
