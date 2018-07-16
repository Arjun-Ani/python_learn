import random
i=0
a=""
while(i<4):
    b=random.choice('1234567890')
    a=a+b
    i=i+1
j=0
cow=0
bull=0
while(j<4):
    c=raw_input("Enter the Digit\n")
    if(int(a[j])==int(c)):
        cow=cow+1
    else:
        bull=bull+1
    print "Cow=%s Bull=%s" %(cow,bull)
    j=j+1

        
