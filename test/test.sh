#!/bin/sh

set -e

python3 ./packadd-runner.py help
python3 ./packadd-runner.py -h
python3 ./packadd-runner.py install https://github.com/morhetz/gruvbox.git
python3 ./packadd-runner.py list
python3 ./packadd-runner.py uninstall gruvbox