a={}
b=raw_input("Enter the number of inputs\n")
i=0
while(i<int(b)):
    d=raw_input("Enter the Name\n")
    c=raw_input("Enter the DOB\n")
    a[d]=c
    i=i+1
print "We know the DOB of" 
for i in a.keys():
    print i
e=raw_input("Enter the name whose DOB should be is played\n")
for i in a.keys():
    if i==e:
        print a[i]

