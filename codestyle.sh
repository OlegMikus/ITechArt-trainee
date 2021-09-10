#!/bin/bash

echo ">>> $(basename ${BASH_SOURCE[0]})"

set -o errexit # exit script when command fails
set -o pipefail # this setting prevents errors in a pipeline from being masked
set -o nounset # exit script when it tries to use undeclared variables

echo 'pylint'
pylint .
echo 'flake8'
flake8 .
echo 'pycodestyle'
pycodestyle --first .
echo 'mypy'
mypy . --exclude migrations

echo ">>> $(basename ${BASH_SOURCE[0]}) DONE"