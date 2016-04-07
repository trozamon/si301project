from __future__ import print_function
import argparse
import datetime


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('input_files',
            type=str,
            nargs='+',
            help='JSON input files of contributors'
            )

    parser.add_argument('output_file',
            type=str,
            help='Output .json file for human consumption'
            )

    return parser.parse_args()


def run(input_repos):
    release_speed = {}

    for r in input_repos:
        msgs = git.Repo(r).get_tag_msgs()
        dates = []

        for msg in msgs:
            for line in msg.split("\n"):
                if re.match('Date:.*\d+ \d+:\d+:\d+ \d\d\d\d'):
                    dates.append(line.replace("Date:   ", ""))

        for date in dates:
            # TODO parse or remove timezone info
            real_date = datetime.strptime(date, "%a %b %d %H:%M:%S %Y")
