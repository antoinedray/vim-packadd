#!/bin/sh

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

info()
{
    printf "usage: packadd [-h | -l | -i | -u | -d]\n"
    exit 1
}

init()
{
    mkdir -p ~/.vim/pack/packages
    cd ~/.vim
    printf '*\n!pack/packages\n' > .gitignore
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

if [ "$#" -ne 1 ]; then
    info
elif [ "$1" = "-h" ]; then
    clear
    printf "\nPACKADD(1)\t\tMy Commands Manual\t\tPACKADD(1)\n"
    printf "\nNAME\n\tpackadd -- vim package manager\n"
    printf "\nSYNOPSIS\n\tpackadd [argument]\n"
    printf "\nDESCRIPTION\n"
    printf "\t-h\thelp\n"
    printf "\t-l\tlist installed packages\n"
    printf "\t-i\tinstall a package\n"
    printf "\t-u\tupdate all packages\n"
    printf "\t-d\tdelete a package\n\n"
    exit 0
elif [ "$1" = "-l" ]; then
    check_init
    ls ~/.vim/pack/packages/start
elif [ "$1" = "-i" ]; then
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
elif [ "$1" = "-u" ]; then
    check_init
    cd ~/.vim
    git submodule update --remote --merge
    git commit -m "Updated packages"
    printf "${GREEN}Packages updated${NC}\n"
    exit 0
elif [ "$1" = "-d" ]; then
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
else
    info
fi
