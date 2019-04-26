# -*- coding: utf-8 -*-


"""tests.tests: provides testing entry point main()."""


import os
import argparse
import unittest
from .packadd import initRepo, install, uninstall, upgrade
from .config import Paths


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.subparser = self.parser.add_subparsers()
        self.pi = self.subparser.add_parser('install')
        self.pi.add_argument('url')
        self.puni = self.subparser.add_parser('uninstall')
        self.puni.add_argument('package')
        self.plist = self.subparser.add_parser('list')

    def testInitRepo(self):
        initRepo()
        self.assertTrue(os.path.isdir(Paths.VIM))

    def testInstall(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbox.git'])
        install(args)
        self.assertTrue(os.path.isdir(Paths.START + '/gruvbox'))

    def testInstallUnexisting(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbo.git'])
        install(args)
        self.assertFalse(os.path.isdir(Paths.START + '/gruvbo'))

    def testUninstall(self):
        args = self.puni.parse_args(['gruvbox'])
        uninstall(args)
        self.assertFalse(os.path.isdir(Paths.START + '/gruvbox'))

    def testUptodateUpgrade(self):
        args = self.pi.parse_args(['https://github.com/tomasr/molokai.git'])
        install(args)
        try:
            upgrade(None)
        except(RuntimeError):
            self.fail("Error triggered on upgrade")


def main():
    unittest.main()
