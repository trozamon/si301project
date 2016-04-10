from __future__ import print_function
from si301 import git
import argparse
from datetime import datetime
import numpy
import re


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('input_files',
            type=str,
            nargs='+',
            help='repo list'
            )

    return parser.parse_args()


def run(input_repos):
    release_speed = {}

    for r in input_repos:
        print("computing for " + r)

        msgs = git.Repo(r).get_tag_msgs()
        dates = []

        for msg in msgs:
            for line in msg.split("\n"):
                if re.match('Date:.*\d+ \d+:\d+:\d+ \d\d\d\d [+-]\d\d\d\d', line):
                    date = datetime.strptime(
                            line.replace("Date:   ", "")[0:-6],
                            "%a %b %d %H:%M:%S %Y"
                            )

                    dates.append(date)

        dates = sorted(dates)
        diffs = []
        for i in range(1, len(dates)):
            prev = dates[i - 1]
            curr = dates[i]
            dt = curr - prev

            diffs.append((float(dt.days) * 24.0) + (float(dt.seconds) / 3600.0))

        d = numpy.array(diffs)
        print(numpy.average(d))

if  __name__ == "__main__":
    run(parse_args().input_files)
