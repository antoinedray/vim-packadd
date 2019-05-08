# -*- coding: utf-8 -*-


"""epita.install: provides installation utility functions."""


import os
import sys
import shutil
from .config import Paths, Aliases


class Utils:
    def __init__(self, automate, debug):
        self.automate = automate
        self.debug = debug

    def initFolders(self, folders):
        for f in folders:
            if not os.path.isdir(f):
                try:
                    os.makedirs(f)
                    print('Folder created at ' + f)
                except Exception as e:
                    print('Could not create folder at ' + f)
                    if self.debug:
                        print('Exception: ' + str(e))
                    sys.exit(1)
            else:
                print('Folder already created at ' + f)

    def moveFile(self, src, dst):
        try:
            shutil.copyfile(src, dst, follow_symlinks=True)
        except Exception as e:
            print('Failed to copy file from ' + src + ' to ' + dst)
            if self.debug:
                print('Exception: ' + str(e))
            sys.exit(1)

    def setPerms(self, path):
        try:
            os.chmod(path, 0o555)
        except Exception as e:
            print('Failed to set permissions on ' + path)
            if self.debug:
                print('Exception: ' + str(e))
            sys.exit(1)

    def patchInstalled():
        if os.path.isfile(Paths.PATCH):
            print('Patch already present on your system...')
            return True
        return False

    def setAlias(self):
        if self.automate or input("\nAdd it automatically ? (y/N) ") == 'y':
            with open(Paths.BASHRC, 'a') as f:
                f.write(Aliases.FULL)
        else:
            print('Please add the following line to your bashrc:\n')
            print('  ' + Aliases.LINKSCRIPT)
            print('  ' + Aliases.PY_BIN + '\n')

    def createSymlink(self, src, dst):
        # The dst folder must not exists when calling symlink but it's path
        # must exists, thus the 2 first lines create the path up to dst
        head, tail = os.path.split(dst)
        Utils.initFolders(self, [head])
        try:
            os.symlink(src, dst)
        except Exception as e:
            print('Failed to create symlink between ' + src + ' and ' + dst)
            print('Check that ' + src + ' exist and ' + dst + ' doesn\'t')
            if self.debug:
                print('Exception: ' + str(e))
            sys.exit(1)

    def addVimToPie(self):
        c = "\nAdd automatically vim folder to install.sh dotfiles ? (y/N) "
        if os.path.isfile(Paths.INSTALL_SH):
            if self.automate or input(c) == 'y':
                with open(Paths.INSTALL_SH) as f:
                    if 'vim' not in f.read():
                        t = f.read().replace('dot_list="', 'dot_list="vim ')
                        with open(Paths.INSTALL_SH, "w") as f:
                            f.write(t)
        else:
            print('Missing file ' + Paths.INSTALL_SH)
