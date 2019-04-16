# -*- coding: utf-8 -*-


"""epita.install: provides packadd install script."""


import os
import sys
import shutil
import subprocess
from .config import Colors, Paths, Aliases


def initFolders():
    if not os.path.isdir(Paths.PIP):
        os.makedirs(Paths.PIP)
        print('Permanent pip folder created at ~/afs/.pip')
    else:
        print('Permanent pip folder already created at ~/afs/.pip')


def moveFile(src, dst):
    shutil.copyfile(src, dst, follow_symlinks=True)


def setPermissions(path):
    os.chmod(path, 0o555)


def patchInstalled():
    if os.path.isfile(Paths.PATCH):
        print('Patch already present on your system')
        return True
    return False


def setAlias():
    print('Please add the following line to your bashrc:\n\n')
    print(Aliases.LINKSCRIPT + '\n')
    if '-y' in sys.argv or input("\nAdd it automatically ? (y/N) ") == 'y':
        with open(Paths.BASHRC, 'a') as f:
            f.write(Aliases.FULL)
        subprocess.call('source ' + Aliases.BASHRC, shell=True)


def main():

    # Check if patch already installed
    if patchInstalled():
        return 0

    initFolders()
    moveFile('packadd-fix.sh', Paths.PATCH)
    setPermissions(Paths.PATCH)
    setAlias()
    # FIXME: add the proposition of updating install.sh to get perm install