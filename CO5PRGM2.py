#2 . Write a python program to copy odd lines of one file to other

		

f=open("mits2.txt")
rfile=[i for i in f]
f.close()
f1=open("mits4.txt","w")
for i in range(0,len(rfile)):
	if i%2!=1:
		f1.write(rfile[i])
