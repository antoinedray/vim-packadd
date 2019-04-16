# -*- coding: utf-8 -*-


"""epita.command: executed when epita installation is asked."""


from setuptools import Command
from .install import main


class epita_install(Command):

    description = 'installation for epita pie'

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        main()
