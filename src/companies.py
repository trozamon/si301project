#!/usr/bin/env python

import json
import networkx
import os
import si301.email
import sys


def run(summary_files):
    g = networkx.Graph()

    for fname in summary_files:
        project_name = os.path.split(fname)[-1].split(".")[0]
        stats = {}

        with open(fname) as f:
            stats = json.loads(f.read())

        for author_addr in stats:
            addr = si301.email.Address(author_addr)
            dom = addr.get_domain()
            if not "\"" in dom:
                g.add_edge(project_name, addr.get_domain())

    output = ["digraph G {"]
    for edge in g.edges():
        output.append("    \"" + edge[0] + "\" -> \"" + edge[1] + "\";")

    output.append("}")

    return u"\n".join(output).encode("utf-8")


if __name__ == "__main__":
    out = run(sys.argv[1:])
    print(out)