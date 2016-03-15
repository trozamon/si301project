#!/usr/bin/env python

from __future__ import print_function
import os
import subprocess
import sys


def cd_cmd(directory, cmd):
    cwd = os.getcwd()

    os.chdir(directory)
    raw = subprocess.check_output(cmd)

    os.chdir(cwd)
    return raw


class GitCommit:

    def __init__(self, path_to_repo, revision):
        raw = cd_cmd(path_to_repo, ["git", "show", "--format=short", revision])

        for line in raw.split("\n"):
            if len(line) > 0 and line.startswith("Author: "):
                self.author = line.replace("Author: ", "")


def print_usage():
    print("""analyze.py <git_repo>""")


def git_rev_list(path_to_repo):
    raw = cd_cmd(path_to_repo, ["git", "rev-list", "--reverse", "HEAD"])
    return raw.split("\n")


if __name__ == "__main__":
    folder = sys.argv[1]
    rev_list = git_rev_list(folder)

    for r in rev_list:
        if len(r) == 0:
            continue

        commit = GitCommit(folder, r)
        print(commit.author)
