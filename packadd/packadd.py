# -*- coding: utf-8 -*-


"""packadd.packadd: provides entry point main()."""


__version__ = "0.5.0"


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


def initFolders():
    if not os.path.isdir(Paths.VIM):
        os.makedirs(Paths.VIM)
    if not os.path.isdir(Paths.START):
        os.makedirs(Paths.START)
    if not os.path.isdir(Paths.OPT):
        os.makedirs(Paths.OPT)


def initRepo():
    with open(Paths.VIM + '.gitignore', 'a') as vim:
        vim.write('*\n!pack/packadd\n')
    repo = git.Repo.init(Paths.VIM)
    repo.git.submodule('init')
    repo.index.commit('Structure initialised')
    print(Prints.PRE_INFO + 'Packadd initialized')


def checkRepo():
    if not os.path.isdir(Paths.VIM):
        initFolders()
    if not os.path.isdir(Paths.START):
        initFolders()
    if not os.path.isdir(Paths.OPT):
        initFolders()
    try:
        git.Repo(Paths.VIM)
    except git.exc.InvalidGitRepositoryError:
        initRepo()


def version(args):
    print('Packadd v' + __version__)


def listAll(args):
    checkRepo()
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
    checkRepo()
    print('\n' + Prints.PRE_INFO + 'Upgrading all packages...\n')
    repo = git.Repo(Paths.VIM)
    repo.submodule_update(init=True, recursive=True, progress=Progress())
    print('\n' + Prints.PRE_OK + 'Packages are up to date\n')


def install(args):
    url = args.url
    if url[-1] == '/':
        url = url[:-1]
    checkRepo()
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
    checkRepo()
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
    version = 'Packadd ' + __version__

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.set_defaults(func=lambda x: parser.print_usage())
    parser.add_argument('-v', '--version', action='version',
                        version=version, help='print version information')
    sp = parser.add_subparsers()

    pinstall = sp.add_parser('install', help='install package from url')
    pinstall.add_argument('url')
    pinstall.set_defaults(func=install)

    plist = sp.add_parser('list', help='list all installed packages')
    plist.set_defaults(func=listAll)

    puninstall = sp.add_parser('uninstall', help='removes selected packages')
    puninstall.add_argument('package')
    puninstall.set_defaults(func=uninstall)

    pupgrade = sp.add_parser('upgrade', help='upgrade all packages')
    pupgrade.set_defaults(func=upgrade)

    args = parser.parse_args()
    args.func(args)
