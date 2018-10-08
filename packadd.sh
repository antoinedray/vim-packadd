#!/bin/sh

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

if [ "$#" -ne 1 ]; then
    printf "[${RED}FAILED${NC}] Usage: packadd -COMMAND (use -h to read the doc)\n"
    exit 1
fi

if [ "$1" = "-h" ]; then
    clear
    printf "\nPACKADD(1)      My Commands Manual      PACKADD(1)\n"
    printf "\nNAME\n"
    printf "    packadd -- vim package manager\n"
    printf "\nSYNOPSIS\n"
    printf "    packadd [argument]\n"
    printf "\nDESCRIPTION\n"
    printf "    -h    help\n"
    printf "    -c    create structure to store packages\n"
    printf "    -u    update all packages\n"
    printf "    -i    install a package\n"
    printf "    -d    delete a package\n\n"
    exit 0
fi

if [ "$1" = "-c" ]; then
    mkdir -p ~/.vim/pack/packages
    cd ~/.vim
    git init
    git submodule init
    printf "[  ${GREEN}OK${NC}  ] Packadd initiated\n"
    exit 0
fi

if [ "$1" = "-i" ]; then
    cd ~/.vim
    printf "[${YELLOW}PROMPT${NC}] Enter package name: "
    read name
    printf "[${YELLOW}PROMPT${NC}] Enter git url: "
    read url
    git submodule add $url pack/packages/start/$name
    git add .gitmodules pack/packages/start/$name
    git commit -m "$name installed"
    printf "[  ${GREEN}OK${NC}  ] $name installed\n"
    exit 0
fi

if [ "$1" = "-u" ]; then
    cd ~/.vim
    git submodule update --remote --merge
    git commit -m "Updated packages"
    printf "[  ${GREEN}OK${NC}  ] Packages updated\n"
    exit 0
fi

if [ "$1" = "-d" ]; then
    cd ~/.vim
    echo -ne "[${YELLOW}PROMPT${NC}] Enter package name: "
    read name
    git submodule deinit pack/packages/start/$name
    git rm pack/packages/start/$name
    rm -Rf .git/modules/vim/pack/packages/start/$name
    git commit -m "$name uninstalled"
    printf "[  ${GREEN}OK${NC}  ] $name uninstalled\n"
    exit 0
fi
