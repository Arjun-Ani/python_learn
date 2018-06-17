a=raw_input("Enter the email address\n")
b=a.split('@')
c=[i.split('.') for i in b]
print "Name = %s" %str(c[0])
print "Company = %s" %c[1][0]
