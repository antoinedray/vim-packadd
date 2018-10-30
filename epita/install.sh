#!/bin/sh

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

if [ ! -d "~/afs/.pip" ]; then
    mkdir ~/afs/.pip
fi

chmod u+x packadd-fix.sh

printf "[ ${YELLOW}INFO${NC} ] Adding patch to .vim folder...\n"

mv packadd-fix.sh ~/afs/.pip/

printf "[ ${YELLOW}INFO${NC} ] Please add the following line to your .bashrc:\n"

printf "\n\talias packadd="/bin/sh ~/afs/.pip/packadd-fix.sh"\n\n"

echo "alias packadd='/bin/sh ~/afs/.pip/packadd-fix.sh'" >> ~/.bashrc