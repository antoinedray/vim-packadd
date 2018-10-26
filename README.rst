Installing Vim packages has never been simpler
=======================================
[![Build Status](https://travis-ci.org/rhysd/vim-clang-format.svg?branch=master)](https://travis-ci.org/rhysd/vim-clang-format)

This python script takes all the pain of installing Vim packages away, one line in the command line is now all it takes !

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
- git

## Install Vim-Packadd

Install Vim-Packadd in 3 easy steps !

```
$ git clone git@github.com:cloudnodes/vim-packadd.git
$ cd vim-packadd
$ pip install .
```

## Usage
#### Installing
```
$ packadd install <url>
```
#### Uninstalling
```
$ packadd uninstall <package-name>
```
#### Upgrading
```
$ packadd upgrade
```
## License

    The MIT License (MIT)

    Copyright (c) 2018 cloudnodes

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
