class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)
l1=int(input("Enter the length of rectangle 1:"))
b1=int(input("Enter the breadth of rectangle 1:"))
r1=Rectangle(l1,b1)
print("Area of rectangle 1 is:",r1.area())
print("Perimeter of rectangle 1 is:",r1.perimeter())
l2=int(input("Enter the length of rectangle 2:"))
b2=int(input("Enter the breadth of rectangle 2:"))
r2=Rectangle(l2,b2)
print("Area of rectangle 2 is:",r2.area())
print("Perimeter of rectangle 2 is:",r2.perimeter())
a1=r1.area()
a2=r2.area()
if a1>a2:
    print("Area of rectangle 1 is higher")
elif a1<a2:
    print("Area of rectangle 2 is higher")
else:
    print("Both the areas are equal")
