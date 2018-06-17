a=input("Enter the limit\n")
b=lambda a: a>0 and b(a-1)+100 or 1
print b(a)
