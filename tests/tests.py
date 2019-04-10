# -*- coding: utf-8 -*-


"""tests.tests: provides testing entry point main()."""


import argparse
import unittest
import os
import sys
import git
sys.path.append("..")
import packadd.packadd as pack
import packadd.config as conf


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.subparser = self.parser.add_subparsers()
        self.pi = self.subparser.add_parser('install')
        self.pi.add_argument('url')
        self.puni = self.subparser.add_parser('uninstall')
        self.puni.add_argument('package')
        self.plist = self.subparser.add_parser('list')

    def test_init_repo(self):
        pack.init_repo()
        self.assertTrue(os.path.isdir(conf.Paths.VIM))

    def test_install(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbox.git'])
        pack.install(args)
        self.assertTrue(os.path.isdir(conf.Paths.START + '/gruvbox'))

    def test_install_unexisting(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbo.git'])
        pack.install(args)
        self.assertFalse(os.path.isdir(conf.Paths.START + '/gruvbo'))

    def test_uninstall(self):
        args = self.puni.parse_args(['gruvbox'])
        pack.uninstall(args)
        self.assertFalse(os.path.isdir(conf.Paths.START + '/gruvbox'))

    def test_uptodate_upgrade(self):
        args = self.pi.parse_args(['https://github.com/tomasr/molokai.git'])
        pack.install(args)
        try:
            pack.upgrade(None)
        except ExceptionType:
            self.fail("Upgrade raised ExceptionType unexpectedly")


def main():
    unittest.main()