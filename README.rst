# VIM Packadd
[![Build Status](https://drone.vbernaud.fr/api/badges/antoinedray/vim-packadd/status.svg)](https://drone.vbernaud.fr/antoinedray/vim-packadd)

Installing Vim packages made simpler
=======================================

This python script takes all the pain of installing Vim packages away, one simple command in the CLI is now all it takes !

This script is based on the all new Vim8 native third-party package loading.

For now this scripts only supports git repositories (ex: vim-airline, gruvbox,...).

Currently the below commands have been implemented:

- install <url> (install package with the given url)
- uninstall <package> (uninstall the package)
- upgrade (upgrade all packages installed with this script)

## Requirements

The following are needed to run the script:

- Vim (version 8+)
- Git (1.7.x or newer)
- Python3 (need to check if runs on python < 3x)
- Pip

## Install Vim-Packadd

Install Vim-Packadd in 1 easy steps !

```bash
pip install vim-packadd --user
```

**Note:** If you already installed packages without packadd, it is recomended to reinstall them so that packadd work on all packages installed on your system.

### Installing for EPITA students
As pip installed packages gets deleted everytime you reboot the computer, I wrote a little script to reisntall the package on the first time you run a packadd command. To install it for Epita's computer, please run:

```bash
git clone https://github.com/cloudnodes/vim-packadd.git
cd vim-packadd
python3 setup.py epita_install -a
source ~/.bashrc
```

### Fixing potential ```command not found``` errors

Python packages often install scripts (executables) as well as Python modules. To get full use of ```--user``` installed packages, you may also want to put the matching executable path onto your system. I do this with the following lines in my ```~/.bashrc``` file:

```bash
export PY_USER_BIN=$(python -c 'import site; print(site.USER_BASE + "/bin")')
export PATH=$PY_USER_BIN:$PATH
```

## Usage
#### Listing
```bash
packadd list
```
#### Installing
```bash
packadd install <url>
```
#### Uninstalling
```bash
packadd uninstall <package_name>
```
#### Upgrading
```bash
packadd upgrade
```
## License

    The MIT License (MIT)

    Copyright (c) 2018 Antoine Dray "antoinedray"

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
