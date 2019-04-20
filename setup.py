# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from setuptools import Command
from .epita.config import Paths
from .epita.utils import Utils


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('packadd/packadd.py').read(),
    re.M
    ).group(1)


with open("README.md", "r") as fh:
    long_description = fh.read()


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
        if Utils.patchInstalled():
            return 0
        Utils.initFolders()
        Utils.moveFile('epita/bind.py', Paths.PATCH)
        Utils.setPerms(Paths.PATCH)
        u.setAlias()
        u.addVimToPie()
        print('Installation finished please run:\n')
        print('  source ' + Paths.BASHRC)


setup(
    name = "vim-packadd",
    packages = ["packadd"],
    cmdclass = {
        'epita_install': epita_install
    },
    entry_points = {
        #'distutils.commands': [
        #    'epita_install = epita.command:epita_install',
        #],
        'console_scripts': ['packadd = packadd.packadd:main'],
    },
    version = version,
    author = "Antoine Dray",
    author_email = "antoine.dray@epita.fr",
    description = "Package manager for Vim8.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    install_requires=[
          'gitpython',
      ],
    url = "https://github.com/antoinedray/vim-packadd",
    test_suite="packadd.tests",
)
