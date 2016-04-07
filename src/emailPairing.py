from __future__ import print_function
import argparse
import json
import si301.git
import sys

import glob
import errno
from pprint import pprint

total_num_commits = 0;
low_val_commits = 0;
#low_val_authors = 0;
#high_val_authors = 0;
high_val_commits = 0;

##authors
d = {}


path = u'build/*.json'
files = glob.glob(path)  
count = 0;
for name in files:
	short = name.rsplit(u'/')[-1]

	newpath = u'build/' + short
	with open(newpath) as data_file:    
		data = json.load(data_file)

		low_val_authors = 0;
		high_val_authors = 0;
		total_num_authorsPerFile = 0;

		for x in data:
			email = x.strip('"')
			for a in data:
				y = a.strip('"')
				if(email == y):
					continue

				if(email < y):
					if(email, y) not in d:
						d[(email, y)] = 1;
					else:
					
						d[(email, y)] = d[(email,y)] + 1;

				else:
					if(y, email) not in d:
						d[(y, email)] = 1;
					else:
						d[(y, email)] = d[(y,email)] + 1;
	count +=1;
	print (count)
	if(count == 5):
		break

			
##total number of authors/commits,
##low volume authors
## low volume commits
## 


##find cluster for companies
##dell, ubuntu for one company
pprint(d)


