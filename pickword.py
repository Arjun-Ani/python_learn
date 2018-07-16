from random import *
words=[]
i=0
with open("/python/sowpods.txt") as f:
    line=f.readline()
    while line:
        i=i+1
        words.append(line)
        line=f.readline()
a=randint(0,i+1)
print words[a].split()
