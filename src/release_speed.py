from __future__ import print_function
from si301 import git
import argparse
from datetime import datetime
import numpy
import sys


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('input_files',
            type=str,
            nargs='+',
            help='repo list'
            )

    parser.add_argument('output_file',
            type=str,
            help='output summary file'
            )

    return parser.parse_args()


def run(input_files, out_file):
    release_speed = {}
    output = []

    for fname in input_files:
        dates = []

        with open(fname) as f:
            for line in f:
                date = None
                line = line.rstrip("\n")

                try:
                    date = datetime.strptime(
                            line.replace("Date:   ", "")[0:-6],
                            "%a %b %d %H:%M:%S %Y"
                            )
                except ValueError:
                    print("failed on \"" + line + "\" in " + fname,
                            file=sys.stderr)

                dates.append(date)

        dates = sorted(dates)
        diffs = []
        for i in range(1, len(dates)):
            prev = dates[i - 1]
            curr = dates[i]
            dt = curr - prev

            diffs.append((float(dt.days) * 24.0) + (float(dt.seconds) / 3600.0))

        d = numpy.array(diffs)
        output.append(fname + ": " + str(numpy.average(d)) + " hours")

    with open(out_file, 'w') as f:
        f.write("\n".join(output))

if  __name__ == "__main__":
    args = parse_args()
    run(args.input_files, args.output_file)
