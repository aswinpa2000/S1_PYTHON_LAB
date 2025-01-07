#Write a program to write a python dictionary to a csv file. After writing the csv file read the csv file and display the contents.

import csv

d=[{'name':'Aswin','rollno':18,'course':'mca'},
    {'name':'Amal','rollno': 29,'course':'mca'},
     {'name':'Akash','rollno':36,'course':'mca'},
     {'name': 'midhun','rollno':34,'course':'mca'}]
    
 
field=['name','rollno','course']

filename=['dict.csv']

with open('dict.csv','w') as file:
	w=csv.DictWriter(file, fieldnames=field)
	w.writeheader()
	w.writerows(d)
with open("dict.csv",mode="r") as file:
	csvr=csv.reader(file)
	for row in csvr:
		print(row)

