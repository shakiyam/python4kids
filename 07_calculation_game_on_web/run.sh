#!/bin/bash
set -eu -o pipefail

[[ $# != 1 ]] && { echo "usage: run.sh PROGRAM_FILE"; exit 1; }

flake8 "$1"
FLASK_APP="$1" FLASK_ENV=development flask run --host=0.0.0.0
