b=input("Enter the limit\n")
j=0
a=[(0,1,j)]
d=map(lambda x:x[2]<b and a.append((x[1],x[0]+x[1],x[2]+1)),a)
print "fibonacci series"
for i in a:
    print i[0]

