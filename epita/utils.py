# -*- coding: utf-8 -*-


"""epita.install: provides installation utility functions."""


import os
import shutil
import subprocess
from .config import Paths, Aliases


def initFolders():
    if not os.path.isdir(Paths.PIP):
        os.makedirs(Paths.PIP)
        print('Permanent pip folder created at ~/afs/.pip')
    else:
        print('Permanent pip folder already created at ~/afs/.pip')


def moveFile(src, dst):
    shutil.copyfile(src, dst, follow_symlinks=True)


def setPerms(path):
    os.chmod(path, 0o555)


def patchInstalled():
    if os.path.isfile(Paths.PATCH):
        print('Patch already present on your system...')
        return True
    return False


def setAlias(auto):
    print('Please add the following line to your bashrc:\n')
    print('\t' + Aliases.LINKSCRIPT)
    print('\t' + Aliases.PY_BIN)
    print('\t' + Aliases.PATH)
    if auto or input("\nAdd it automatically ? (y/N) ") == 'y':
        with open(Paths.BASHRC, 'a') as f:
            f.write(Aliases.FULL)
        subprocess.run('source ' + Paths.BASHRC, shell=True, check=True)
