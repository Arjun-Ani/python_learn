def prime(p):
    i=2
    while(i<int(a)):
        if(int(a)%i==0):
            print i
            p=1
        i=i+1
    return p

a=raw_input("Enter the number to be checked\n")
p=0
k=prime(p)
if(k==0):
    print "prime"
else:
    print "composite"
