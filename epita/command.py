# -*- coding: utf-8 -*-


"""epita.command: defines the epita installation."""


from setuptools import Command
from .config import Paths
from .utils import Utils


class epita_install(Command):

    description = 'installation for epita pie'

    user_options = [
        ('automate', 'a', 'fully automate installation'),
        ('debug', 'd', 'enables debug for installation')
    ]

    def initialize_options(self):
        self.automate = None
        self.debug = None

    def finalize_options(self):
        pass

    def run(self):
        u = Utils(self.automate is not None)
        if Utils.patchInstalled():
            return 0
        Utils.initFolders([Paths.PIP, Paths.BIN, Paths.VIM])
        Utils.moveFile('epita/bind.py', Paths.PATCH)
        Utils.setPerms(Paths.PATCH)
        u.setAlias()
        Utils.createSymlink(Paths.VIM, Paths.CONF_VIM)
        u.addVimToPie()
        print('Installation finished please run:\n')
        print('  source ' + Paths.BASHRC + '\n')
