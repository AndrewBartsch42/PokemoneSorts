import numpy
from pokemon import pokemon
import csv

with open ('Pokemon_numerical.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
