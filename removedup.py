def list_input(a):
    i=0
    c=[]
    d=[]
    while(i<a):
        e=raw_input("Enter the element\n")
        c.append(e)
        i=i+1
    d=c
    j=0
    while(j<a):
        k=j+1
        while(k<a):
            if(c[j]==c[k]):
                c.pop(k)
                a=a-1
            k=k+1
        j=j+1
    return c
a=raw_input("Enter the number of elements in the list\n")
b=list_input(int(a))
print b
