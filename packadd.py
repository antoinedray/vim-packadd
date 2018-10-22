import os
import git

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
    PRE = c.INFO + c.BOLD + '> ' + c.ENDC

vim_dir = '~/.vim'
vim_packages = '~/.vim/pack/packages'

def init_repo():
    if not os.path.exists(vim_packages):
        os.makedirs(vim_packages)
    with open(vim_dir + '.gitignore', 'a') as vim:
        vim.write('*\n!pack/packages\n')
    repo = git.Repo.init(vim_packages)
    sub = repo.git.submodule('init')
    print(p.PRE + 'Packadd initiated')

def update():
    repo = git.Repo.init(vim_packages)
    sub = repo.git.submodule('update', '--remote', '--merge')
    repo.commit
    print(p.PRE + 'Packages updated')


def install():
    repo = git.Repo.clone_from(self._small_repo_url(), os.path.join(rw_dir, 'repo'), branch='master')