def list_input(a):
    i=0
    c=[]
    while(i<a):
        d=raw_input("Enter the element\n")
        c.append(d)
        i=i+1
    d=[]
    d.append(c[0])
    d.append(c[i-1])
    return d
a=raw_input("Enter the length of the list\n")
b=list_input(int(a))
print b
