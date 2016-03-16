#!/usr/bin/env python

from __future__ import print_function
import json
import si301.git
import sys


def print_usage():
    print("""analyze.py <git_repo>""")


if __name__ == "__main__":
    folder = sys.argv[1]
    repo = si301.git.Repo(folder)
    authors = repo.get_authors()
    contribs = {}

    for auth in authors:
        contribs[str(auth.email)] = auth.contributions[repo.project]

    print(json.dumps(contribs, sort_keys=True, indent=2))
