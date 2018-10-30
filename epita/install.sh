#!/bin/sh

FAIL='\033[0;31m'
OK='\033[0;32m'
INFO='\033[0;33m'
NC='\033[0m' # No Color

if [ -f "~/afs/.pip/packadd-fix.sh" ]; then
    printf "[ ${INFO}INFO${NC} ] File already installed\n"
    exit 0
else
    if [ ! -d "~/afs/.pip" ]; then
        mkdir ~/afs/.pip
    fi

    chmod u+x packadd-fix.sh

    printf "[ ${INFO}INFO${NC} ] Adding patch to .pip folder...\n"

    mv packadd-fix.sh ~/afs/.pip/

    printf "[ ${INFO}INFO${NC} ] Adding alias to your .bashrc\n"

    echo "# Setup for Vim Packadd, do not remove" >> ~/.bashrc
    echo "alias packadd='/bin/sh ~/afs/.pip/packadd-fix.sh'" >> ~/.bashrc

    printf "[ ${INFO}INFO${NC} ] Reloading bashrc\n"

    source ~/.bashrc

    printf "[  ${OK}OK${NC}  ] Installation successfull\n"
fi
