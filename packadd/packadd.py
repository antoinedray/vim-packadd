# -*- coding: utf-8 -*-


"""packadd.packadd: provides entry point main()."""

__version__ = "0.1.0"

import os, sys, git

argc = len(sys.argv)

class c:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    OK = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class p:
    PRE_INFO = c.INFO + c.BOLD + '> ' + c.END
    PRE_OK = c.OK + c.BOLD + '> ' + c.END
    INV_USAGE = c.FAIL + 'Error:' + c.END + ' Invalid usage: '
    USAGE = 'Example usage:\n  packadd install FORMULA...\n  packadd upgrade\n  packadd uninstall FORMULA...'
    UNKNOWN = c.FAIL + 'Error:' + c.END + ' Unknown command: '

vim_dir = os.environ['HOME'] + '/.vim'
start_packages = os.environ['HOME'] + '/.vim/pack/packages/start/'
opt_packages = os.environ['HOME'] + '/.vim/pack/packages/opt/'

def create_structure():
    if not os.path.isdir(start_packages):
        os.makedirs(start_packages)
    if not os.path.isdir(opt_packages):
        os.makedirs(opt_packages)

def init_repo():
    with open(vim_dir + '.gitignore', 'a') as vim:
        vim.write('*\n!pack/packages\n')
    repo = git.Repo.init(vim_dir)
    sub = repo.git.submodule('init')
    print(p.PRE_INFO + 'Packadd initialized')

def check_repo():
    if not os.path.isdir(start_packages) or not os.path.isdir(opt_packages):
       create_structure()
    try:
        git.Repo(vim_dir)
    except git.exc.InvalidGitRepositoryError:
        init_repo()

def upgrade():
    check_repo()
    print(p.INFO + 'Upgrading all packages...')
    repo = git.Repo(vim_dir)
    repo.submodule_update(recursive=False)
    print(p.PRE_OK + 'Packages updated')

def install():
    if argc < 3:
        print(p.INV_USAGE + 'This command requires an url')
        return
    url = sys.argv[2]
    check_repo()
    print(p.INFO + 'Installing...')
    name = os.path.splitext(os.path.basename(url))[0]
    repo = git.Repo(vim_dir)
    repo.create_submodule(name=name, path=start_packages + name, url=url, branch='master')
    repo.index.commit(name + ' installed')
    print(p.PRE_OK + name + ' installed')

def uninstall():
    if argc < 3:
        print(p.INV_USAGE + 'This command requires a package name')
        return
    name = sys.argv[2]
    check_repo()
    print(p.INFO + 'Uninstalling ' + name + '...')
    repo = git.Repo(vim_dir)
    for sm in repo.submodules:
        if sm.name == name:
            sm.remove()
            repo.index.commit(name + ' uninstalled')
            print(p.PRE_OK + name + ' uninstalled')
            return
    print(c.FAIL + 'Error:' + c.END + ' Unknown package: ' + name)

def main():
    if len(sys.argv) < 2:
        print(p.USAGE)
        return
    cmd = sys.argv[1]
    if cmd == 'upgrade':
        upgrade()
    elif cmd == 'install':
        install()
    elif cmd == 'uninstall':
        uninstall()
    else:
        print(p.UNKNOWN + cmd)