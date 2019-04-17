# -*- coding: utf-8 -*-


"""epita.install: provides installation utility functions."""


import os
import shutil
from .config import Paths, Aliases


class Utils:
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

    def createSymlink():
        os.symlink(Paths.VIM, Paths.CONF_VIM)

    def addVimToPie():
        c = "\nAdd automatically vim folder to install.sh dotfiles ? (y/N) "
        if os.path.isfile(Paths.INSTALL_SH)
            if auto or input(c) == 'y':
                with open(Paths.INSTALL_SH) as f:
                    t = f.read().replace('dot_list="', 'dot_list="vim ')
                with open(Paths.INSTALL_SH, "w") as f:
                    f.write(t)


