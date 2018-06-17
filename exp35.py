class circle(object):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return "Area = %s" %(3.14*(self.radius**2))
a=input("Enter the radius\n")
b=circle(a)
print b.area()
