#!/bin/bash
set -e
DEFAULT_PATH=$1

if [ "$MODE" = "production" ]; then
    echo "Installing dependencies"
    pip3 install -r ${DEFAULT_PATH}/production.txt
    echo "Requirements installed!\n"
else
    echo "Installing dependencies"
    pip3 install -r ${DEFAULT_PATH}/development.txt
fi

exit 0
