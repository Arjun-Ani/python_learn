a=raw_input("Enter the String\n")
l=[(i,a.count(i)) for i in a]
print dict(l)
