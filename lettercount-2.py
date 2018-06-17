a=raw_input("Enter the sentence\n")
b=a.split(' ')
c=[(i,b.count(i)) for i in b ]
print list(set(c))
