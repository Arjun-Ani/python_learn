a=input("Enter the Limit\n")
b=[input("Enter the element\n") for i in range(a)]
d=input("Enter the Element to be searched\n")
c=sorted(b)
e=lambda x,y:d>x[y/2] and e(x[(y+1)/2:],y/2) or (d<x[y/2] and e(x[:y/2],y/2) or x[y/2])
print e(c,a)
#print c[:a/2]

