#5. Create a class Publisher (name). Derive class Book from Publisher with attributes title and author. Derive class Python from Book with attributes price and no_of_pages. Write a program that displays information about a Python book. Use base class constructor invocation and method overriding.


#Parent class
class Publisher:
	def __init__(self,name):
		self.name = name
	def display():
		pass
		
			
#child class	
class Book(Publisher):
	def __init__(self,name,title,author):
		#Base class conctructor
		super().__init__(name)
		self.title = title
		self.author = author
	def display():
		pass			
class Python(Book):
	def __init__(self,name,title,author,price,no_of_pages):
		super().__init__(name,title,author)
		self.price = price
		self.no_of_pages = no_of_pages
	def display(self):
		print(".....Book details.....")
		print("Name :",self.name)
		print("Title :",self.title)
		print("Name :",self.author)
		print("Price :",self.price)
		print("Number of pages :",self.no_of_pages)
		
name = input("Enter the name : ")
title = input("Enter the title :")
author = input("Enter the author :")
price = int(input("Enter the price :"))
no_of_pages =  input("Enter the no of pages : ")
b = Python(name,title,author,price,no_of_pages)
b.display()		
		
			
	
		
					
