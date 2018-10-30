#!/bin/sh

# Packadd
python3 -m site &> /dev/null && PATH="$PATH:`python3 -m site --user-base`/bin"

command_exists () {
    type "$1" &> /dev/null ;
}

packadd_fix() {
    if ! command_exists packadd; then
        pip install --user vim-packadd >&-
    fi
}

packadd_fix;

\packadd
