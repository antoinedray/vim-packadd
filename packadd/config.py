# -*- coding: utf-8 -*-


"""packadd.config: provides packadd configurations."""


import os


class path:
    VIM = os.environ['HOME'] + '/.vim'
    START = os.environ['HOME'] + '/.vim/pack/packadd/start/'
    OPT = os.environ['HOME'] + '/.vim/pack/packadd/opt/'


class colors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    OK = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[31m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class prints:
    PRE_INFO = colors.INFO + colors.BOLD + '> ' + colors.END
    PRE_INFO_L = colors.INFO + colors.BOLD + '==> ' + colors.END
    PRE_FAIL = colors.FAIL + colors.BOLD + '> ' + colors.END
    PRE_FAIL_L = colors.FAIL + colors.BOLD + '==> ' + colors.END
    PRE_OK = colors.OK + colors.BOLD + '> ' + colors.END
    PRE_OK_L = colors.OK + colors.BOLD + '==> ' + colors.END
    PRE_LIST = colors.INFO + colors.BOLD + '  - ' + colors.END
