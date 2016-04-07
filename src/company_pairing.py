from __future__ import print_function
import argparse
import json
import si301.git
import si301.mailmap
import sys

import glob
import errno
from pprint import pprint

##authors
collabs = {}
count = 0

files = glob.glob(u'build/*.json')  
for fname in files:
    print("working on " + fname, file=sys.stderr)

    project = fname.rsplit(u'/')[-1].split('.')[0]
    companies = set()

    with open(fname) as data_file:    
        data = json.load(data_file)

        for email in data:
            company = si301.mailmap.get_company(email)
            if len(company) > 0:
                companies.add(company)

    print("found " + str(len(companies)) + " companies", file=sys.stderr)

    # make sure the list does not contain duplicates
    companies = list(companies)

    for i in range(len(companies)):
        j = i + 1

        while j < len(companies):
            tmp = sorted([companies[i], companies[j]])

            try:
                collabs[(tmp[0], tmp[1])] = collabs[(tmp[0], tmp[1])] + 1
            except KeyError:
                collabs[(tmp[0], tmp[1])] = 1

            j = j + 1

for collab in collabs:
    print(str(collabs[collab]) + " <-> " + str(collab))
