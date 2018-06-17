def maxim(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    if c>a and c>b:
        return c
a=raw_input("Enter the First number\n")
b=raw_input("Enter the Second number\n")
c=raw_input("Enter the Third number\n")
d=maxim(int(a),int(b),int(c))
print "Largest Number %s" %d

