Installing Vim packages has never been simpler
=======================================
[![Build Status](http://82.66.68.210/api/badges/antoinedray/vim-packadd/status.svg)](http://82.66.68.210/antoinedray/vim-packadd)

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
- python3 (need to check if runs on python < 3x)
- pip
- git

## Install Vim-Packadd

Install Vim-Packadd in 1 easy steps !

```
pip install vim-packadd --user
```

**Note:** If you already installed packages without packadd, it is recomended to reinstall them so that packadd work on all packages installed on your system.

### Installing for EPITA students
First and foremost, you need to make Vim packages persistent on the afs, to do so:\
Create the vim folder:
```
mkdir ~/afs/config/vim && mkdir ~/.vim
```
Create symlink between the two folders:
```
ln -s ~/.vim ~/afs/.confs/vim
```
Then, add the *vim* folder to the install.sh in ~/afs/config/install.sh

As pip installed packages gets deleted everytime you reboot the computer, I wrote a little script to reisntall the package on the first time you run a packadd command. To install it for Epita's computer, please run:

```
git clone https://github.com/cloudnodes/vim-packadd.git
cd vim-packadd/epita
./install.sh
```

## Usage
#### Listing
```
packadd list
```
#### Installing
```
packadd install <url>
```
#### Uninstalling
```
packadd uninstall <package_name>
```
#### Upgrading
```
packadd upgrade
```
## License

    The MIT License (MIT)

    Copyright (c) 2018 Antoine Dray "cloudnodes"

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
