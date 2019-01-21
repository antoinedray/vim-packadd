#!/bin/sh

FAIL='\033[0;31m'
OK='\033[0;32m'
INFO='\033[0;33m'
NC='\033[0m' # No Color

if [ -f "~/afs/.pip/packadd-fix.sh" ]; then
    printf "[${INFO}INFO${NC}] File already installed\n"
    exit 0
fi

if [ ! -d "~/afs/.pip" ]; then
    mkdir ~/afs/.pip
    if [ "$?" -eq 0 ]; then
        printf "[ ${OK}OK${NC} ] Created ~/afs/.pip dir successfully\n"
    else
        printf "[${FAIL}FAIL${NC}] Could not create ~/afs/.pip dir\n"
    fi
fi

chmod u+x packadd-fix.sh
if [ "$?" -eq 0 ]; then
    printf "[ ${OK}OK${NC} ] Applied execution rights to packadd-fix.sh successfully\n"
else
    printf "[${FAIL}FAIL${NC}] Could not apply execution rights to packadd-fix.sh\n"
    exit 1
fi

printf "[${INFO}INFO${NC}] Adding patch to .pip folder...\n"

mv packadd-fix.sh ~/afs/.pip/
if [ "$?" -eq 0 ]; then
    printf "[ ${OK}OK${NC} ] Added patch to .pip folder successfully\n"
else
    printf "[${FAIL}FAIL${NC}] Could not move packadd runtime script to ~/afs/.pip/\n"
    exit 1
fi

printf "[${INFO}INFO${NC}] Adding alias to your .bashrc\n"

echo "# Setup for Vim Packadd, do not remove" >> ~/.bashrc
echo "alias packadd='/bin/sh ~/afs/.pip/packadd-fix.sh'" >> ~/.bashrc

printf "[${INFO}INFO${NC}] Reloading bashrc\n"

source ~/.bashrc
if [ "$?" -eq 0 ]; then
    printf "[ ${OK}OK${NC} ] Reloaded bashrc successfully\n"
else
    printf "[${FAIL}FAIL${NC}] Could not reload bashrc, please do it manually\n"
fi

printf "[ ${OK}OK${NC} ] Installation successfull\n"

exit 0
