a=raw_input("Enter the number\n")
b=int(a)/2
i=1
c=[]
while i<=int(b):
    if int(a)%i==0:
        c.append(i)
    i=i+1
print c


