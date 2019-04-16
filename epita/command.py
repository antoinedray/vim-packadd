# -*- coding: utf-8 -*-


"""epita.command: executed when epita installation is asked."""


from setuptools import Command
from .install import main


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
        main(self.automate is not None)
