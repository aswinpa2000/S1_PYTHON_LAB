# Create reactangle class with attributes length and breadth and methods to find area and perimeter. Compare two rectangle objects by their areas.

class Rectangle:
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
	def area(self):
		return self.length * self.breadth
	def perimeter(self):
		return 2*(self.length + self.breadth)	
		
length = int(input("Enter the length : "))
breadth = int(input("Enter the breadth : "))
rect1 = Rectangle(length,breadth)

length = int(input("Enter the length : "))
breadth = int(input("Enter the breadth : "))

print("Rectangle 1")
print("Area of rectangle : ",rect1.area())
print("Perimeter of rectangle : ",rect1.perimeter())
rect2 = Rectangle(length,breadth)
print("Rectangle 2")
print("Area of rectangle : ",rect2.area())
print("Perimeter of rectangle : ",rect2.perimeter())


if rect1.area() > rect2.area():
	print("Area of rect1 is greater")
elif rect2.area() > rect1.area():
	print("Area of rect2 is greater")
else:
	print("Area of both reactangle are equal")				
