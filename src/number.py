from __future__ import print_function
import argparse
import json
import si301.git
import sys

import glob
import errno

total_num_commits = 0;
low_val_commits = 0;
#low_val_authors = 0;
#high_val_authors = 0;
high_val_commits = 0;

##authors
per_file_high_val =  {}
per_file_low_val =  {}
per_file_total_authors = {}


path = u'build/*.json'
files = glob.glob(path)  
for name in files:
	short = name.rsplit(u'/')[-1]

	newpath = u'build/' + short
	with open(newpath) as data_file:    
		data = json.load(data_file)

		low_val_authors = 0;
		high_val_authors = 0;
		total_num_authorsPerFile = 0;

		for email in data:

			num = data[email]
			##Email contributed less than 5 times to this file
			if(num < 5):
				low_val_authors += 1;
			else:
				high_val_authors += 1;

			total_num_authorsPerFile += 1;



		per_file_high_val[short] = high_val_authors
		per_file_low_val[short] = low_val_authors
		print(total_num_authorsPerFile)
		per_file_total_authors[short] =total_num_authorsPerFile;
##total number of authors/commits,
##low volume authors
## low volume commits
## 


##find cluster for companies
##dell, ubuntu for one company




print("\n\n\n High Value Authors\n\n\n")
for key in per_file_high_val:

	## X authors out of total # Y authors that contribute more than 5 times
    print ("File: ", key, 'corresponds to this number of high value authors', per_file_high_val[key], ' percentage of total: ', per_file_high_val[key]/float(per_file_total_authors[key]))
print ("\n\n\n Low Value Authors\n\n\n")

for key in per_file_low_val:
	#X authors out of total # Y authors that contribute less than 5 times
    print ("File: ", key, 'corresponds to this number of low value authors', per_file_low_val[key], ' percentage of total: ', per_file_low_val[key]/float(per_file_total_authors[key]))
