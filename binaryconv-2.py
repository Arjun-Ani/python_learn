a=[raw_input("Enter the 4 digit binary number\n") for i in range(4)]
p=[]
for i in a:
    l=0
    k=3
    for j in i:
        l=l+(int(j)*(2**k))
        k=k-1
    p.append(l)
k=[i for i in p if i%5==0]
print k

