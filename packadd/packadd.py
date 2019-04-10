# -*- coding: utf-8 -*-


"""packadd.packadd: provides entry point main()."""


__version__ = "0.4.0"


import os
import git
import re
import argparse
from .config import Colors, Paths, Prints


class Progress(git.remote.RemoteProgress):
    msg = ''

    def update(self, op_code, cur_count, max_count, message):
        rate = (cur_count / max_count * 100, 100)[cur_count == 0]
        pre = (Prints.PRE_INFO_L, Prints.PRE_OK_L)[match(message, '^Done')]
        if not message:
            message = Progress.msg
            line = pre + ' ({:.0f}%) {:<65}'.format(rate, message)
            print(line + ('', '...')[len(message) > 65], end='\r')
        else:
            Progress.msg = message
            print(pre + ' ({:.0f}%) '.format(rate) + message)


def match(line, regex):
    reg = re.compile(regex)
    if re.match(reg, line):
        return 1
    return 0


def init_folders():
    if not os.path.isdir(Paths.START):
        os.makedirs(Paths.START)
    if not os.path.isdir(Paths.OPT):
        os.makedirs(Paths.OPT)


def init_repo():
    with open(Paths.VIM + '.gitignore', 'a') as vim:
        vim.write('*\n!pack/packadd\n')
    repo = git.Repo.init(Paths.VIM)
    repo.git.submodule('init')
    repo.index.commit('Structure initialised')
    print(Prints.PRE_INFO + 'Packadd initialized')


def check_repo():
    if not os.path.isdir(Paths.START) or not os.path.isdir(Paths.OPT):
        init_folders()
    try:
        git.Repo(Paths.VIM)
    except git.exc.InvalidGitRepositoryError:
        init_repo()


def listall(args):
    check_repo()
    repo = git.Repo(Paths.VIM)
    print(Prints.PRE_INFO + 'Listing...')
    if not repo.submodules:
        print(Prints.PRE_INFO + 'No packages installed yet')
    else:
        print()
        for sm in repo.submodules:
            print(Prints.PRE_LIST + sm.name)
        print()


def upgrade(args):
    check_repo()
    print('\n' + Prints.PRE_INFO + 'Upgrading all packages...\n')
    repo = git.Repo(Paths.VIM)
    repo.submodule_update(init=True, recursive=False, progress=Progress())
    print('\n' + Prints.PRE_OK + 'Packages are up to date\n')


def install(args):
    url = args.url
    if url[-1] == '/':
        url = url[:-1]
    check_repo()
    print(Prints.PRE_INFO + 'Installing...')
    name = os.path.splitext(os.path.basename(url))[0]
    repo = git.Repo(Paths.VIM)
    try:
        if '--opt' in args:
            fpath = Paths.OPT
        else:
            fpath = Paths.START + name
        repo.create_submodule(name=name, path=fpath, url=url, branch='master')
        repo.index.commit(name + ' installed')
        print(Prints.PRE_OK + name + ' installed')
    except git.exc.GitCommandError:
        print(Prints.PRE_FAIL + 'Invalid git package url')


def uninstall(args):
    name = args.package
    check_repo()
    print(Prints.PRE_INFO + 'Uninstalling ' + name + '...')
    repo = git.Repo(Paths.VIM)
    for sm in repo.submodules:
        if sm.name == name:
            sm.remove()
            repo.index.commit(name + ' uninstalled')
            print(Prints.PRE_OK + name + ' uninstalled')
            return
    print(Colors.FAIL + 'Error:' + Colors.END + ' Unknown package: ' + name)


def main():
    parser = argparse.ArgumentParser()
    sp = parser.add_subparsers()

    pinstall = sp.add_parser('install', help='install package from url')
    pinstall.add_argument('url')
    pinstall.set_defaults(func=install)

    plist = sp.add_parser('list', help='list all installed packages')
    plist.set_defaults(func=listall)

    puninstall = sp.add_parser('uninstall', help='removes selected packages')
    puninstall.add_argument('package')
    puninstall.set_defaults(func=uninstall)

    pupgrade = sp.add_parser('upgrade', help='upgrade all packages')
    pupgrade.set_defaults(func=upgrade)

    args = parser.parse_args()
    args.func(args)
