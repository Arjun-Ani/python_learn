a=raw_input("Enter the Number of transactions\n")
b=[raw_input("Enter the transaction\n") for i in range(int(a))]
c=[i.split(' ') for i in b]
money=0
d=dict(c)
for i in d.iteritems():
    if i[0]=="D":
        money=money+int(i[1])
    if i[0]=="W":
        money=money-int(i[1])

print "Remaining Balance=%s" %money

