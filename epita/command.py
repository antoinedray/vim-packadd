# -*- coding: utf-8 -*-


"""epita.command: executed when epita installation is asked."""


from setuptools import Command
from .install import main


class epita_install(Command):

    description = 'installation for epita pie'

    def run(self):
        main()
