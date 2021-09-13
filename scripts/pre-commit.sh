#!/bin/bash

echo ">>> $(basename ${BASH_SOURCE[0]})"

set -o errexit # exit script when command fails
set -o pipefail # this setting prevents errors in a pipeline from being masked
set -o nounset # exit script when it tries to use undeclared variables



# INIT WORKING DIR
# ===================================================
cd "$(dirname "${BASH_SOURCE[0]}")"
FILE_DIR=$(pwd)
cd ..
CWD="$(pwd)"

cd "${CWD}"
cp -f "${CWD}/hooks/pre-commit.sh" "${CWD}/.git/hooks/pre-commit"
chmod ug+x "${CWD}/.git/hooks/pre-commit"