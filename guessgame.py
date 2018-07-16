from random import *
a=raw_input("Enter the number in your mind\n")
b=randint(1,100)
print b
print a
if(int(a)==b):
    print "You guessed it correct"
elif(int(a)<b):
    print "Guessed it more"
else:
    print "Guessed it less"
