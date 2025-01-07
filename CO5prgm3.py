# Write a program to read each row from the csv file and print a list of strings.

import csv
with open("student.csv",mode="r") as file:
	csvr = csv.reader(file)
	for row in csvr:
		#print(row)
		#print(row[2])
		print(row[1])

