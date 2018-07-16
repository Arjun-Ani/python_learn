import random
def guess(n):
    print n
    a=raw_input("Enter your guess(1-9)\n")
    b=random.randrange(1,10)
   # n[0]=n[0]+1
   # print b
    if(a=="exit"):
        print "Thank You :-)"
        print n
        #return n
    elif(int(a)==b):
        print "Congrats you made correct guess :-)"
        n[1]=n[1]+1
        n[0]=n[0]+1
        print n
        guess(n)
    elif(int(a)<b):
        print "Unfortunately less"
        n[2]=n[2]+1
        n[0]=n[0]+1
        print n
        guess(n)
    else:
        print "Unfortunately Greater"
        n[2]=n[2]+1
        n[0]=n[0]+1
        print n
        guess(n)
    return n
    #print "Failed attempts %s" %fail
    #print "Successfull attempts %s" %suc
   # return no,suc,fail
#no=0
#suc=0
#fail=0
n=[0,0,0]
#f=[0,0,0]
h=guess(n)
print h
#print f
print "Number of attempts %s" %h[0]
print "Number of success %s" %h[1]
print "Number of failure %s" %h[2]


