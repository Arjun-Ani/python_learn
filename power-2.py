class square(object):
    def __init__(self,num):
        self.num=num
    def calc(self):
        return self.num**2
a=input("Enter the number whose power has to be found\n")
b=square(a)
print "Square is %s" %b.calc()
