a=raw_input("Enter the column\n")
b=raw_input("Enter the row\n")
i=0
k=0
m=0
c=""
d=""
while (m<int(b)):
    while(i<int(a)):
        c=c+" "
        for j in xrange(1,4):
            c=c+"-"
        i=i+1
    while(k<int(a)):
        d=d+"|"
        for l in xrange(1,4):
            d=d+" "
        k=k+1
    m=m+1
    print c
    print d+"|"
print c
