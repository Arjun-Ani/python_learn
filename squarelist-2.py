a=input("Enter the number of row\n")
b=input("Enter the number of column\n")
c=map(lambda x:[x[0]+x[2]*i for i in range(x[1])],[(0,b,j)for j in range(a)])
print c

