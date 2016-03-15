#!/usr/bin/env python

from __future__ import print_function
import si301.git
import os
import subprocess
import sys


def print_usage():
    print("""analyze.py <git_repo>""")


if __name__ == "__main__":
    folder = sys.argv[1]
    repo = si301.git.Repo(folder)
