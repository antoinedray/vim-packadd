# -*- coding: utf-8 -*-


"""bind: defines the epita fix script."""


import os
#import pip
from pip._internal import install
import sys
import site
import subprocess as sp


def isInstalled():
    if os.path.isdir(site.USER_SITE):
        with os.scandir(site.USER_SITE) as d:
            for entry in d:
                if 'vim-packadd' in str(entry):
                    return True
    return False


def pipInstall(package):
    install(['install', package])
    #if hasattr(pip, 'main'):
    #pip.main(['install', package])
    #else:
    #    pip._internal.main(['install', package])


def main():
    cmd = sys.argv
    #cmd[0] = '\\' + cmd[0]
    #print(cmd)

    if not isInstalled():
        print('Reinstalling...')
        pipInstall('vim-packadd --user')

    process = sp.Popen(cmd, stdout=sp.PIPE)
    for line in process.stdout.readlines():
        print(line, flush=True)
    process.communicate()[0]
    return process.returncode

main()
