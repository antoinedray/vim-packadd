# -*- coding: utf-8 -*-


"""epita.command: defines the epita installation."""


from setuptools import Command
from .config import Paths
from .utils import Utils


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
        u = Utils(self.automate is not None)
        if u.patchInstalled():
            return 0
        u.initFolders()
        u.moveFile('epita/bind.py', Paths.PATCH)
        u.setPerms(Paths.PATCH)
        u.setAlias()
        u.addVimToPie()
        print('Installation finished please run:\n')
        print('  source ' + Paths.BASHRC)
