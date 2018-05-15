a=raw_input("Enter the string to be reversed\n")
b=a.split()
c=len(b)
i=c-1
d=[]
while(i>=0):
    d.append(b[i])
    i=i-1
a=""
for i in d:
    a=a+i+" "
print a
