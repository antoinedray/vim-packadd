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

vim_dir = '~/.vim'
vim_packages = '~/.vim/pack/packages'

def init_repo():
    if not os.path.exists(vim_packages):
        os.makedirs(vim_packages)
    with open(vim_dir + '.gitignore', 'a') as vim:
        vim.write('*\n!pack/packages\n')
    r = git.Repo.init(vim_packages)

    print(c.INFO + 'Packadd initiated' + c.END)