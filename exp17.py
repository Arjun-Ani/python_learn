a=raw_input("Enter the Number of transactions\n")
b=[raw_input("Enter the transaction\n") for i in range(int(a))]
c=[i.split(' ') for i in b]
print dict(c)

