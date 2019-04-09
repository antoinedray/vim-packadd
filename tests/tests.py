# -*- coding: utf-8 -*-


"""tests.tests: provides testing entry point main()."""


import argparse
import unittest
import os
import sys
sys.path.append("..")
import packadd.packadd as pack


class path:
    VIM = os.environ['HOME'] + '/.vim'
    START = os.environ['HOME'] + '/.vim/pack/packadd/start/'
    OPT = os.environ['HOME'] + '/.vim/pack/packadd/opt/'


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.subparser = self.parser.add_subparsers()
        self.pi = self.subparser.add_parser('install')
        self.pi.add_argument('url')
        self.puni = self.subparser.add_parser('uninstall')
        self.puni.add_argument('package')

    def test_install(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbox.git'])
        pack.install(args)
        self.assertTrue(os.path.isdir(path.START + '/gruvbox'))

    def test_uninstall(self):
        args = self.puni.parse_args(['gruvbox'])
        pack.uninstall(args)
        self.assertFalse(os.path.isdir(path.START + '/gruvbox'))


def main():
    unittest.main()