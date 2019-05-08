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
        automate = self.automate is not None
        debug = self.debug is not None
        u = Utils(automate, debug)
        if Utils.patchInstalled():
            return 0
        u.initFolders([Paths.PIP, Paths.BIN, Paths.VIM])
        u.moveFile('packadd/packadd.sh', Paths.PATCH)
        u.setPerms(Paths.PATCH)
        u.setAlias()
        u.createSymlink(Paths.VIM, Paths.CONF_VIM)
        u.addVimToPie()
        print('Installation finished please run:\n')
        print('  source ' + Paths.BASHRC + '\n')
