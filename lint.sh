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

PY_FILES=$(find . -type f -name "*.py" ! -path './.*' -not -path "**/migrations/*" -not -path "**/settings/*")

echo '>>> running pylint'
pylint --load-plugins pylint_flask $PY_FILES

echo '>>> running flake8'
flake8 $PY_FILES

echo '>>> running pycodestyle'
pycodestyle --first $PY_FILES

echo '>>> running mypy'
mypy $PY_FILES --exclude migrations

echo ">>> $(basename ${BASH_SOURCE[0]}) DONE"