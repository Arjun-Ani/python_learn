a=raw_input("Enter the number of elements in the list\n")
i=0
c=[]
while i<int(a):
    b=raw_input("Enter the element\n")
    c.append(b)
    i=i+1
d=[]
for i in c:
    if(float(i)%2==0):
        d.append(i)
print d
