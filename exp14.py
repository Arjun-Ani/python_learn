a=raw_input("Enter the Input\n")
upper=0
lower=0
for i in a:
    if i.isupper():
        upper=upper+1
    if i.islower():
        lower=lower+1
print "Upper Letter\'s %s" %upper
print "Lower Letter\'s %s" %lower

