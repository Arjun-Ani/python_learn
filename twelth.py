def fib(a):
    i=1
    j=1
    f=[]
    f.append(i)
    while(j<a):
        f.append(j)
        #f.append(j)
        k=i+j
        i=j
        j=k
    return f

a=raw_input("Enter the limit\n")
b=fib(int(a))
print b
