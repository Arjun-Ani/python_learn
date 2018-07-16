a=[]
with open("/python/happynumbers.txt") as f:
    line=f.readline()
    while line:
        a.append(int(line))
        line=f.readline()
b=[]
with open("/python/primenumbers.txt") as f:
    line=f.readline()
    while(line):
        b.append(int(line))
        line=f.readline()
c=[]
for i in a:
    for j in b:
        if(i==j):
            c.append(i)
print c




