#!/usr/bin/env python

from __future__ import print_function
import argparse
import json
import si301.git
import sys


def print_usage():
    print("""analyze.py <git_repo>""")


def parse_args():
    parser = argparse.ArgumentParser(
            description='Analyze a git repo and generate a list of authors'
            )

    parser.add_argument('path_to_repo',
            type=str,
            help='path to a version control repository'
            )

    parser.add_argument('output_file',
            type=str,
            help='path to output file'
            )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    repo = si301.git.Repo(args.path_to_repo)

    print("retrieving all authors...", file=sys.stderr)
    authors = repo.get_authors_fast()

    with open(args.output_file, 'w') as f:
        f.write(json.dumps(authors, sort_keys=True, indent=2))
