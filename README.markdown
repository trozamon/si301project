# SI 301 Project

Analysis of the social network that develops various open source software, with
a focus on the core operating system software of GNU/Linux.

This repository has a lot of submodules; running `git submodule update` for the
first time will take a **long** time. It will also require quite a bit of disk
space - around 2 GiB.

## Running the Code
There is a `Makefile` that will run the analysis. In order to get all the
python packages, `venv.sh` and `requirements.txt` are provided. `venv.sh` sets
up a python virtual environment with all the necessary stuff. In order to run
the code, run:

    source venv.sh
    make

## Running the tests
Running the tests is possible with:

    make check

## Software List

* autoconf 2.69
* automake 1.15
* bash 4.3
* binutils 2.26
* bison 3.0.4
* coreutils 8.25
* cpio 2.12
* curl 7.48.0
* dbus 1.9.20
* emacs 24.5
* gawk 4.1.3
* gcc 5.3.0
* ghostscript 9.14.0
* git 2.7.3
* gnupg 2.1.11
* grep 2.24
* gzip 1.6
* httpd 2.4.18
* linux 4.5
* make 4.1
* polkit 0.113
* screen 4.3.1
* sed 4.2.2
* systemd 229
* tar 1.28
* wget 1.17.1
