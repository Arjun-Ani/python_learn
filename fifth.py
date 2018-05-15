a=raw_input("Enter the number of elements in first list\n")
b=raw_input("Enter the number of elements in second list\n")
c=[]
d=[]
def list_input(a):
    c=[]
    i=0
    while(i<int(a)):
        d=raw_input("enter the element\n")
        c.append(d)
        i=i+1
    return c
print "first list"
c=list_input(a)
print "second list"
d=list_input(b)
e=[]
for i in c:
    for j in d:
        if(i==j):
            e.append(i)
print e


