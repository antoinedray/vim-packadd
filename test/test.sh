#!/bin/sh

set -e

packadd list
packadd help
packadd -h
packadd install https://github.com/morhetz/gruvbox.git
packadd list
packadd upgrade
packadd uninstall gruvbox