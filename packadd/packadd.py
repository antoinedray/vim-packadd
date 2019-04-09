# -*- coding: utf-8 -*-


"""packadd.packadd: provides entry point main()."""


__version__ = "0.3.11"

import os
import git
import re
import argparse


class path:
    VIM = os.environ['HOME'] + '/.vim'
    START = os.environ['HOME'] + '/.vim/pack/packadd/start/'
    OPT = os.environ['HOME'] + '/.vim/pack/packadd/opt/'


class c:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    OK = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[31m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class p:
    PRE_INFO = c.INFO + c.BOLD + '> ' + c.END
    PRE_INFO_L = c.INFO + c.BOLD + '==> ' + c.END
    PRE_FAIL = c.FAIL + c.BOLD + '> ' + c.END
    PRE_FAIL_L = c.FAIL + c.BOLD + '==> ' + c.END
    PRE_OK = c.OK + c.BOLD + '> ' + c.END
    PRE_OK_L = c.OK + c.BOLD + '==> ' + c.END
    PRE_LIST = c.INFO + c.BOLD + '  - ' + c.END


class Progress(git.remote.RemoteProgress):
    msg = ''

    def update(self, op_code, cur_count, max_count, message):
        rate = (cur_count / max_count * 100, 100)[cur_count == 0]
        pre = (p.PRE_INFO_L, p.PRE_OK_L)[match(message, '^Done')]
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


def create_folders():
    if not os.path.isdir(path.START):
        os.makedirs(path.START)
    if not os.path.isdir(path.OPT):
        os.makedirs(path.OPT)


def init_repo():
    with open(path.VIM + '.gitignore', 'a') as vim:
        vim.write('*\n!pack/packadd\n')
    repo = git.Repo.init(path.VIM)
    repo.git.submodule('init')
    repo.index.commit('Structure initialised')
    print(p.PRE_INFO + 'Packadd initialized')


def check_repo():
    if not os.path.isdir(path.START) or not os.path.isdir(path.OPT):
        create_folders()
    try:
        git.Repo(path.VIM)
    except git.exc.InvalidGitRepositoryError:
        init_repo()


def listall(args):
    check_repo()
    repo = git.Repo(path.VIM)
    print(p.PRE_INFO + 'Listing...')
    if not repo.submodules:
        print(p.PRE_INFO + 'No packages installed yet')
    else:
        print()
        for sm in repo.submodules:
            print(p.PRE_LIST + sm.name)
        print()


def upgrade(args):
    check_repo()
    print('\n' + p.PRE_INFO + 'Upgrading all packages...\n')
    repo = git.Repo(path.VIM)
    repo.submodule_update(init=True, recursive=False, progress=Progress())
    print('\n' + p.PRE_OK + 'Packages are up to date\n')


def install(args):
    url = args.url
    if url[-1] == '/':
        url = url[:-1]
    check_repo()
    print(p.PRE_INFO + 'Installing...')
    name = os.path.splitext(os.path.basename(url))[0]
    repo = git.Repo(path.VIM)
    try:
        if '--opt' in args:
            fpath = path.OPT
        else:
            fpath = path.START + name
        repo.create_submodule(name=name, path=fpath, url=url, branch='master')
        repo.index.commit(name + ' installed')
        print(p.PRE_OK + name + ' installed')
    except git.exc.GitCommandError:
        print(p.PRE_FAIL + 'Invalid git package url')


def uninstall(args):
    name = args.package
    check_repo()
    print(p.PRE_INFO + 'Uninstalling ' + name + '...')
    repo = git.Repo(path.VIM)
    for sm in repo.submodules:
        if sm.name == name:
            sm.remove()
            repo.index.commit(name + ' uninstalled')
            print(p.PRE_OK + name + ' uninstalled')
            return
    print(c.FAIL + 'Error:' + c.END + ' Unknown package: ' + name)


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
