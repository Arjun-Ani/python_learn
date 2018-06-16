class cla():
    def __init__(self,limit):
        self.limit=limit
    def iter(self):
        c=[i for i in range(self.limit) if i%7==0 ]
        return c
a=input("Enter the limit\n")
b=cla(a)
print b.iter()

