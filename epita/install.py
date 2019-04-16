# -*- coding: utf-8 -*-


"""epita.install: provides packadd install script."""


import os
from .config import Colors, Paths, Prints

def patchInstalled():
    if os.path.isfile(Paths.PATCH):
        print('Patch already present on your system')
        return True
    return False


def initFolders():
    if not os.path.isdir(Paths.PIP):
        os.makedirs(Paths.PIP)
        print('Permanent folder created at ~/afs/.pip')
