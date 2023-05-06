#!/bin/sh
set -e
echo "############################################"
echo "Checking for errors on Pylint..."
bandit --skip B311 -r $INPUT_BASEPATH/
echo "############################################"
