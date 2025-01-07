#3. Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to compare the area of 2 rectangles.

class Rectangle:
	def __init__(self,length,width):
		self.length = length
		self.width = width
	def area(self):
		return self.length * self.width
		
	def __lt__(self,other):
		return self.area() < other.area()
		

a,b = map(int,input("Enter the length and width of first rectangle:").split())
c,d = map(int,input("Enter the length and width of second rectangle:").split())
rect1 = Rectangle(a,b)
rect2 = Rectangle(c,d)	
	
if rect1 < rect2:
	print("Area of rectangle1 is smaller than area of rectangle2")
elif rect1 > rect2:
	print("Area of rectangle1 is larger than area of rectangle2")
else:
	print("Both rectangle have same area")					
