a=[]
print "Enter the sentence"
while True:
    b=raw_input()
    if b:
        a.append(b.upper())
    else:
        break;
for i in a:
    print i
