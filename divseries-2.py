a=input("Enter the limit\n")
b=lambda x: x>0 and (float(x)/float(x+1))+b(x-1) or 0
print b(a)
