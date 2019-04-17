# -*- coding: utf-8 -*-


"""epita.command: defines the epita installation."""


from setuptools import Command
from .config import Paths
from .utils import initFolders, moveFile, setPerms, patchInstalled, setAlias


class epita_install(Command):

    description = 'installation for epita pie'

    user_options = [
        ('automate', 'a', 'fully automate installation')
    ]

    def initialize_options(self):
        self.automate = None

    def finalize_options(self):
        pass

    def run(self):
        # Check if patch already installed
        if patchInstalled():
            return 0
        initFolders()
        moveFile('epita/bind.py', Paths.PATCH)
        setPerms(Paths.PATCH)
        setAlias(self.automate is not None)
        print('Installation finished please run:\n')
        print('  source ' + Paths.BASHRC)
        # FIXME: add the proposition of updating install.sh to get perm install
