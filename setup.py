# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from distutils.core import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('packadd/packadd.py').read(),
    re.M
    ).group(1)


setup(
    name = "vim-packadd",
    packages = ["packadd"],
    entry_points = {
        "console_scripts": ['packadd = packadd.packadd:main']
        },
    version = version,
    description = "Package manager for Vim8.",
    author = "Antoine Dray",
    author_email = "antoine.dray@epita.fr",
    license='MIT',
    install_requires=[
          'gitpython',
      ],
    url = "https://github.com/cloudnodes/vim-packadd",
    )
