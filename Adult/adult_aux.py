import numpy as np
x = []
y = []

import csv
import sys

# open coordinates csv
def read_data_training():
	with open("data.csv") as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			person = []
			print len(row)
			for i in range (0, 13):
				person.append(row[i])
			x.append(person)
			y.append(row[14])
