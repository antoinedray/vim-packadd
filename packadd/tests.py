# -*- coding: utf-8 -*-


"""tests.tests: provides testing entry point main()."""


import os
import argparse
import unittest
import shlex as sh
import subprocess as sp
from .packadd import init_repo, install, uninstall, upgrade
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

    def test_init_repo(self):
        init_repo()
        self.assertTrue(os.path.isdir(Paths.VIM))

    def test_no_args(self):
        cmd = sh.split('python3 packadd-runner.py')
        child = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        child.communicate()[0]
        self.assertEqual(child.returncode, 0)

    def test_invalid_arg(self):
        cmd = sh.split('python3 packadd-runner.py unknown')
        child = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        child.communicate()[0]
        self.assertEqual(child.returncode, 0)

    def test_invalid_args(self):
        cmd = sh.split('python3 packadd-runner.py unknown -h')
        child = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        child.communicate()[0]
        self.assertEqual(child.returncode, 0)

    def test_undefined_command(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbox.git'])

    def test_install(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbox.git'])
        install(args)
        self.assertTrue(os.path.isdir(Paths.START + '/gruvbox'))

    def test_install_unexisting(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbo.git'])
        install(args)
        self.assertFalse(os.path.isdir(Paths.START + '/gruvbo'))

    def test_uninstall(self):
        args = self.puni.parse_args(['gruvbox'])
        uninstall(args)
        self.assertFalse(os.path.isdir(Paths.START + '/gruvbox'))

    def test_uptodate_upgrade(self):
        args = self.pi.parse_args(['https://github.com/tomasr/molokai.git'])
        install(args)
        try:
            upgrade(None)
        except(RuntimeError):
            self.fail("Error triggered on upgrade")


def main():
    unittest.main()
