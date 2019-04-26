# -*- coding: utf-8 -*-


"""epita.config: provides packadd install configurations."""


import os
import site
import platform


class Colors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    OK = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[31m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Paths:
    BASHFILE = ('.bash_profile', '.bashrc')[platform.system() == 'Linux']
    BASHRC = os.environ['HOME'] + '/' + BASHFILE
    PATCH = os.environ['HOME'] + '/afs/.pip/bind.py'
    PIP = os.environ['HOME'] + '/afs/.pip'
    VIM = os.environ['HOME'] + '/.vim'
    CONF_VIM = os.environ['HOME'] + '/afs/.confs/.vim'
    START = os.environ['HOME'] + '/.vim/pack/packadd/start/'
    OPT = os.environ['HOME'] + '/.vim/pack/packadd/opt/'
    BIN = site.USER_BASE + '/bin'
    INSTALL_SH = os.environ['HOME'] + '/afs/.confs/install.sh'


class Aliases:
    COMMENT = '\n# Setup for Vim Packadd, do not remove\n'
    LINKSCRIPT = "alias packadd='python3 ~/afs/.pip/bind.py'"
    PY_BIN = 'export PATH=' + Paths.BIN + ':$PATH'
    FULL = COMMENT + LINKSCRIPT + '\n' + PY_BIN + '\n'
