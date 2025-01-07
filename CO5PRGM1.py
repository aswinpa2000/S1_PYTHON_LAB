#1 .write a program to read a file line by line and store into a list

file = open("mits.txt","r")
l =  [i.split() for i in open ("mits.txt") ]
print(l)
file.close()
