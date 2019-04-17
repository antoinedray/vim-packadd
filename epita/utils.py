# -*- coding: utf-8 -*-


"""epita.install: provides installation utility functions."""


import os
import shutil
from .config import Paths, Aliases


def initFolders():
    if not os.path.isdir(Paths.PIP):
        os.makedirs(Paths.PIP)
        print('Permanent pip folder created at ~/afs/.pip')
    else:
        print('Permanent pip folder already created at ~/afs/.pip')
    if not os.path.isdir(Paths.BIN):
        os.makedirs(Paths.BIN)
        print('PY_BIN path created at ' + Paths.BIN)
    else:
        pprint('PY_BIN already path created at ' + Paths.BIN)



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
    print('  ' + Aliases.LINKSCRIPT)
    print('  ' + Aliases.PY_BIN)
    if auto or input("\nAdd it automatically ? (y/N) ") == 'y':
        with open(Paths.BASHRC, 'a') as f:
            f.write(Aliases.FULL)
