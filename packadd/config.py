# -*- coding: utf-8 -*-


"""packadd.config: provides packadd configurations."""


import os


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
    VIM = os.environ['HOME'] + '/.vim'
    START = os.environ['HOME'] + '/.vim/pack/packadd/start/'
    OPT = os.environ['HOME'] + '/.vim/pack/packadd/opt/'


class Prints:
    PRE_INFO = Colors.INFO + Colors.BOLD + '> ' + Colors.END
    PRE_INFO_L = Colors.INFO + Colors.BOLD + '==> ' + Colors.END
    PRE_FAIL = Colors.FAIL + Colors.BOLD + '> ' + Colors.END
    PRE_FAIL_L = Colors.FAIL + Colors.BOLD + '==> ' + Colors.END
    PRE_OK = Colors.OK + Colors.BOLD + '> ' + Colors.END
    PRE_OK_L = Colors.OK + Colors.BOLD + '==> ' + Colors.END
    PRE_LIST = Colors.INFO + Colors.BOLD + '  - ' + Colors.END
