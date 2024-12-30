
class Rectangle:
   def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
   def area(self):
       return (self.length * self.breadth)
   def perimeter(self):
      return 2 * (self.length + self.breadth)
   def compare(self,other):
       if self.length==other.length:
           return "Same"
       else:
           return "different"
r1=Rectangle(10,3)
r2=Rectangle(10,3)
r1.area()
r1.perimeter()
print("area and perimeter is:",r1.area(),r1.perimeter())
r2.area()
r2.perimeter()
print("area and perimeter is:", r2.area(),r2.perimeter())
print(r1.compare(r2))


