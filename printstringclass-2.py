class Strng(object):
    def __init__(self,a):
        self.a =a
    def printString(self):
        print self.a
a=raw_input("Enter the string\n")
ob=Strng(a)
ob.printString()
