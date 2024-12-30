class studentt:
    tutor_name = "bindu miss"
    def __init__(self,n,a):
        self.name=n
        self.age = a
    def display(self):
        print(self.name)
        print(self.age)
        print(studentt.tutor_name)
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
s1 = studentt("neethu", 20)
s1.display()
s2 = studentt("anju", 20)
s2.display()
print(s1.compare(s2))
