import numpy as np
X = []
y = []

import csv
import sys

# open coordinates csv
with open("toCartesian.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        passToCart[int(row[0])] = [int(row[1]), int(row[2])]