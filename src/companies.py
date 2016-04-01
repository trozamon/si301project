#!/usr/bin/env python

from __future__ import print_function
from si301 import email, mailmap
import argparse
import json
import networkx
import os
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='generate company graphic')

    parser.add_argument('input_files',
            type=str,
            nargs='+',
            help='JSON input files of contributors'
            )

    parser.add_argument('output_file',
            type=str,
            help='Output .dot file for graphviz'
            )

    return parser.parse_args()


def run(summary_files):
    g = networkx.Graph()

    for fname in summary_files:
        project_name = os.path.split(fname)[-1].split(".")[0]
        stats = {}

        with open(fname) as f:
            stats = json.loads(f.read())

        for author_addr in stats:
            dom = mailmap.get_company(author_addr)
            if len(dom) > 0:
                g.add_edge(project_name, dom)

    output = ["digraph G {"]
    for edge in g.edges():
        output.append("    \"" + edge[0] + "\" -> \"" + edge[1] + "\";")

    output.append("}")

    return u"\n".join(output).encode("utf-8")


if __name__ == "__main__":
    args = parse_args()

    print('doing mad graph analytics...', file=sys.stderr)
    out = run(args.input_files)

    print('writing output to ' + args.output_file, file=sys.stderr)
    with open(args.output_file, 'w') as f:
        f.write(out)
