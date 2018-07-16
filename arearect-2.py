class rectangle(object):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return "Area = %s" %(self.length*self.breadth)
a=input("Enter the length of rectangle\n")
b=input("Enter the bradth of rectangle\n")
c=rectangle(a,b)
print c.area()
