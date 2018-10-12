#!/bin/sh

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

if [ "$#" -ne 1 ]; then
    printf "usage: packadd [-h | -i | -u | -d]\n"
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

init()
{
    mkdir -p ~/.vim/pack/packages
    cd ~/.vim
    git init
    git submodule init
    printf "${YELLOW}Packadd initiated${NC}\n"
}

check_init()
{
    if [ ! -d ~/.vim/pack/packages ]; then
        printf "Initiating packadd...\n"
        init
    fi
}

if [ "$1" = "-i" ]; then
    check_init
    cd ~/.vim
    printf "Enter git url: "
    read url
    file="${url##*/}"
    name="${file%.git}"
    git submodule add $url pack/packages/start/$name
    git add .gitmodules pack/packages/start/$name
    git commit -m "$name installed"
    printf "${GREEN}${name} installed${NC}\n"
    exit 0
fi

if [ "$1" = "-u" ]; then
    check_init
    cd ~/.vim
    git submodule update --remote --merge
    git commit -m "Updated packages" >&- # >&- Hides output of cmd
    printf "${GREEN}Packages updated${NC}\n"
    exit 0
fi

if [ "$1" = "-d" ]; then
    check_init
    cd ~/.vim
    echo -ne "Enter package name: "
    read name
    git submodule deinit pack/packages/start/$name
    git rm pack/packages/start/$name
    rm -Rf .git/modules/vim/pack/packages/start/$name
    git commit -m "${name} uninstalled"
    printf "${GREEN}${name} uninstalled${NC}\n"
    exit 0
fi
