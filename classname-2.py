class name(object):
    def __init__(self,name):
        self.name=name
    def message(self):
        return "Hi %s" %self.name
a=raw_input("Enter Your Name\n")
b=name(a)
print b.message()

