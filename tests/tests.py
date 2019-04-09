# -*- coding: utf-8 -*-


"""tests.tests: provides testing entry point main()."""


import argparse
import unittest
import os
import sys
import git
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
        self.plist = self.subparser.add_parser('list')

    def test_install(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbox.git'])
        pack.install(args)
        self.assertTrue(os.path.isdir(path.START + '/gruvbox'))

    def test_install_unexisting(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbo.git'])
        pack.install(args)
        self.assertFalse(os.path.isdir(path.START + '/gruvbo'))

    def test_uninstall(self):
        args = self.puni.parse_args(['gruvbox'])
        pack.uninstall(args)
        self.assertFalse(os.path.isdir(path.START + '/gruvbox'))

    def test_upgrade(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbox.git'])
        repo = git.Repo(path.VIM).submodules[0]
        # Reset our working tree 10 commits into the past
        past_branch = repo.create_head('past_branch', 'HEAD~3')
        repo.head.reference = past_branch
        assert not repo.head.is_detached
        # reset the index and working tree to match the pointed-to commit
        repo.head.reset(index=True, working_tree=True)
        pack.upgrade(args)


def main():
    unittest.main()