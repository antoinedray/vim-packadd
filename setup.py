# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('packadd/packadd.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "vim-packadd",
    packages = ["packadd"],
    entry_points = {
        "console_scripts": ['packadd = packadd.packadd:main']
        },
    version = version,
    description = "Plugin manager for Vim8.",
    long_description = long_descr,
    author = "Antoine Dray",
    author_email = "antoine.dray@epita.fr",
    license='MIT',
    install_requires=[
          'gitpython',
      ],
    url = "https://github.com/cloudnodes/vim-packadd",
    )
