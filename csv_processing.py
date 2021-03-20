#!/usr/bin/env python3

import csv

with open('/home/renardelyon/puisi.csv','r') as unproc:
	with open('/home/renardelyon/puisi_proc.csv','w',newline="") as proc:
		writer = csv.writer(proc)
		reader = csv.reader(unproc)
		next(reader)
		for row in reader:
			if any(row):	
				writer.writerow(row)
