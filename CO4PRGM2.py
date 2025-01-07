# 2. Create a Bank account with members account number, name, type of account and balance. Write constructor and methods to deposit at the bank and withdraw an amount from the bank.

class account:
	def __init__(self,acc_no,name,toc,bal):
		self.acc_no = acc_no
		self.name = name
		self.toc = toc
		self.bal = bal
		
	def deposit(self,amt):
		if amt > 0:
			self.bal = self.bal + amt
			print("Successfully Deposited Amount")
		else:
			print("Invalid amount")	
		
	def withdraw(self,amt):
		if amt > self.bal:
			print("Insufficient Balance")
		else:
			print("Successfully Withdrawn")
			self.bal = self.bal - amt
	def viewDetails(self):
		print("Name :",self.name)
		print("Acount number : ",self.acc_no)
		print("Balance :",self.bal)
		print("Type of Account :",self.toc)		 			
		
a = int(input("Enter the account number : \n"))
n = input("Enter the Name : \n")		
toc = input("Enter type of account : \n")
bal = int(input("Enter balance :\n"))
c1 = account(a,n,toc,bal)
while True:
	print("\nMENU\n1.Deposit\n2.Withdraw\n3.Current Balance\n4.View Details\n5.Exit")
	ch = int(input("Enter your choice : \n"))
	if ch==1:
		amt = int(input("Enter the amount to be deposited : "))
		c1.deposit(amt)
	elif ch==2:
		amt = int(input("Enter the amount to be withdrawn : "))
		c1.withdraw(amt)
	elif ch==3:
		print("Current balance = ",c1.bal)
	elif ch==4:
		c1.viewDetails()
	elif ch==5:
		break
	else:
		print("invalid")
						
		
		
	
