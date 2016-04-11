from __future__ import print_function
from si301 import email, mailmap
import argparse
import json
import networkx
import os
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='generate company contribution percents')

    parser.add_argument('input_files',
            type=str,
            nargs='+',
            help='JSON input files of contributors'
            )

    parser.add_argument('output_file',
            type=str,
            help='output CSV file for google sheets'
            )

    return parser.parse_args()


def run(summary_files):
    output = []

    for fname in summary_files:
        total = 0
        organization = 0
        project_name = os.path.split(fname)[-1].split(".")[0]
        stats = {}

        with open(fname) as f:
            stats = json.loads(f.read())

        for author_addr in stats:
            org = mailmap.get_company(author_addr)
            if len(org) > 0:
                organization = organization + stats[author_addr]

            total = total + stats[author_addr]
        
        output.append(project_name + "," +
                str(float(organization) / float(total)))


    return u"\n".join(output)


if __name__ == "__main__":
    args = parse_args()

    out = run(args.input_files)

    with open(args.output_file, 'w') as f:
        f.write(out)
