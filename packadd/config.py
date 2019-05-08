# -*- coding: utf-8 -*-


"""epita.config: provides packadd install configurations."""


import os
import site
import platform


class Aliases:
    COMMENT = '\n# Setup for Vim Packadd, do not remove\n'
    LINKSCRIPT = "alias packadd='/bin/sh ~/afs/.pip/packadd.sh'"
    PY_BIN = 'export PATH=' + Paths.BIN + ':$PATH'
    FULL = COMMENT + LINKSCRIPT + '\n' + PY_BIN + '\n'


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
    PATCH = os.environ['HOME'] + '/afs/.pip/packadd.sh'
    PIP = os.environ['HOME'] + '/afs/.pip'
    VIM = os.environ['HOME'] + '/.vim'
    CONF_VIM = os.environ['HOME'] + '/afs/.confs/.vim'
    START = os.environ['HOME'] + '/.vim/pack/packadd/start/'
    OPT = os.environ['HOME'] + '/.vim/pack/packadd/opt/'
    BIN = site.USER_BASE + '/bin'
    INSTALL_SH = os.environ['HOME'] + '/afs/.confs/install.sh'


class Prints:
    PRE_INFO = Colors.INFO + Colors.BOLD + '> ' + Colors.END
    PRE_INFO_L = Colors.INFO + Colors.BOLD + '==> ' + Colors.END
    PRE_FAIL = Colors.FAIL + Colors.BOLD + '> ' + Colors.END
    PRE_FAIL_L = Colors.FAIL + Colors.BOLD + '==> ' + Colors.END
    PRE_OK = Colors.OK + Colors.BOLD + '> ' + Colors.END
    PRE_OK_L = Colors.OK + Colors.BOLD + '==> ' + Colors.END
    PRE_LIST = Colors.INFO + Colors.BOLD + '  - ' + Colors.END
