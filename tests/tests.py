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

    def test_upgrade(self):
        args = self.pi.parse_args(['https://github.com/morhetz/gruvbox.git'])
        pack.install(args)
        repo = git.Repo(conf.Paths.VIM)
        sms = repo.submodules
        if len(sms) < 1:
            self.assertTrue(False)
            return
        sm = sms[0]
        # Reset our working tree 3 commits into the past
        sm.git.revert("28205e2497ecf474a4c41d19f2f7cc9543d061f7", no_edit = True)
        #past_branch = sm.create_head('past_branch', 'HEAD~3')
        #sm.head.reference = past_branch
        #assert not sm.head.is_detached
        # reset the index and working tree to match the pointed-to commit
        sm.head.reset(index=True, working_tree=True)
        pack.upgrade(args)


def main():
    unittest.main()