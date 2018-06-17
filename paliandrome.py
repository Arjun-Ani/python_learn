a=raw_input("Enter the string\n")
b=len(a)
c=""
while b>0:
    c=c+a[b-1]
    b=b-1
if(a==c):
    print "paliandrome"
else:
    print "not paliandrome"
