#!/bin/sh

# Packadd
python3 -m site &> /dev/null && PATH="$PATH:`python3 -m site --user-base`/bin"

command_exists() {
    echo "$1"
    type "$1" &> /dev/null ;
}

packadd_fix() {
    if ! command_exists packadd; then
        echo "packdd does not yet exists"
        $(pip install --user vim-packadd)
    fi
}

packadd_fix;

# Runs actual packadd program
\packadd $@