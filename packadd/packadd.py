# -*- coding: utf-8 -*-


"""packadd.packadd: provides entry point main()."""

__version__ = "0.3.2"

import os, sys, git

argc = len(sys.argv)

class path:
    VIM = os.environ['HOME'] + '/.vim'
    START = os.environ['HOME'] + '/.vim/pack/packages/start/'
    OPT = os.environ['HOME'] + '/.vim/pack/packages/opt/'

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
    PRE_FAIL = c.FAIL + c.BOLD + '> ' + c.END
    PRE_OK = c.OK + c.BOLD + '> ' + c.END
    PRE_LIST = c.INFO + c.BOLD + '  - ' + c.END
    INV_USAGE = c.FAIL + 'Error:' + c.END + ' Invalid usage: '
    USAGE = 'Example usage:\n  packadd install [URL]\n  packadd upgrade\n  packadd uninstall [PACKAGE]'
    FURTH_HELP = 'Further help:\n  https://github.com/cloudnodes/vim-packadd'
    UNKNOWN = c.FAIL + 'Error:' + c.END + ' Unknown command: '


def help():
    print(p.USAGE + '\n\n' + p.FURTH_HELP)

def create_structure():
    if not os.path.isdir(path.START):
        os.makedirs(path.START)
    if not os.path.isdir(path.OPT):
        os.makedirs(path.OPT)

def init_repo():
    with open(path.VIM + '.gitignore', 'a') as vim:
        vim.write('*\n!pack/packages\n')
    repo = git.Repo.init(path.VIM)
    sub = repo.git.submodule('init')
    repo.index.commit('Structure initialised')
    print(p.PRE_INFO + 'Packadd initialized')

def check_repo():
    if not os.path.isdir(path.START) or not os.path.isdir(path.OPT):
       create_structure()
    try:
        git.Repo(path.VIM)
    except git.exc.InvalidGitRepositoryError:
        init_repo()

def listall():
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

def upgrade():
    check_repo()
    print(p.PRE_INFO + 'Upgrading all packages...')
    repo = git.Repo(path.VIM)
    repo.submodule_update(recursive=False)
    print(p.PRE_OK + 'Packages updated')

def install():
    if argc != 3:
        print(p.INV_USAGE + 'This command requires an url')
        return
    url = sys.argv[2]
    check_repo()
    print(p.PRE_INFO + 'Installing...')
    name = os.path.splitext(os.path.basename(url))[0]
    repo = git.Repo(path.VIM)
    try:
        repo.create_submodule(name=name, path=path.START + name, url=url, branch='master')
        repo.index.commit(name + ' installed')
        print(p.PRE_OK + name + ' installed')
    except git.exc.GitCommandError:
        print(p.PRE_FAIL + 'Invalid git package url')

def uninstall():
    if argc < 3:
        print(p.INV_USAGE + 'This command requires a package name')
        return
    name = sys.argv[2]
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
    if len(sys.argv) < 2:
        help()
        return
    cmd = sys.argv[1]
    if cmd == 'upgrade':
        upgrade()
    elif cmd == 'install':
        install()
    elif cmd == 'uninstall':
        uninstall()
    elif cmd == 'list':
        listall()
    elif cmd == 'help' or cmd == '-h':
        help()
    else:
        print(p.UNKNOWN + cmd)