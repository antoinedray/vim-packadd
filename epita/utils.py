# -*- coding: utf-8 -*-


"""epita.install: provides installation utility functions."""


import os
import sys
import shutil
from .config import Paths, Aliases


class Utils:
    def __init__(self, a):
        self.automate = a

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
            print('PY_BIN already path created at ' + Paths.BIN)
        if not os.path.isdir(Paths.VIM):
            os.makedirs(Paths.VIM)
        if not os.path.isdir(Paths.CONF_VIM):
            os.makedirs(Paths.CONF_VIM)

    def moveFile(src, dst):
        shutil.copyfile(src, dst, follow_symlinks=True)

    def setPerms(path):
        try:
            os.chmod(path, 0o555)
        except Exception as e:
            print('Failed to set permissions on ' + path)
            sys.exit(1)

    def patchInstalled():
        if os.path.isfile(Paths.PATCH):
            print('Patch already present on your system...')
            return True
        return False

    def setAlias(self):
        print('Please add the following line to your bashrc:\n')
        print('  ' + Aliases.LINKSCRIPT)
        print('  ' + Aliases.PY_BIN)
        if self.automate or input("\nAdd it automatically ? (y/N) ") == 'y':
            with open(Paths.BASHRC, 'a') as f:
                f.write(Aliases.FULL)

    def createSymlink(src, dst):
        try:
            os.symlink(src, dst)
        except Exception as e:
            print('Failed to create symlink between ' + src + ' and ' + dst)
            sys.exit(1)

    def addVimToPie(self):
        c = "\nAdd automatically vim folder to install.sh dotfiles ? (y/N) "
        if os.path.isfile(Paths.INSTALL_SH):
            if self.automate or input(c) == 'y':
                with open(Paths.INSTALL_SH) as f:
                    if not 'vim' in f.read():
                        t = f.read().replace('dot_list="', 'dot_list="vim ')
                        with open(Paths.INSTALL_SH, "w") as f:
                            f.write(t)
        else:
            print('Missing file ' + Paths.INSTALL_SH)
