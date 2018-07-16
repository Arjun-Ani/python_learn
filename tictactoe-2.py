from random import *
def create_multilists():
    b=[]
    c=[]
    for i in range(1,4):
        b=[]
        for j in range(1,4):
            a=randint(0,2)
            b.append(a)
        c.append(b)
    return c
d=create_multilists()
k=[]
for i in range(0,3):
    q=0
    p=0
    for j in range(0,3):
        if(d[i][j]==0):
            p=1
        if(d[j][i]==0):
            q=1
    if d[i][j]==d[i][j-1] and d[i][j]==d[i][j-2] and p==0:
        k.append(d[i][j])
    if d[j][i]==d[j-1][i] and d[j][i]==d[j-2][i] and p==0:
        k.append(d[j][i])
if d[i][i]==d[i-1][i-1]==d[i-2][i-2]!=0:
    k.append(d[i][j])
if d[i-2][j]==d[i-1][j-1]==d[i][j-2]!=0:
    k.append(d[i-2][j])
fp=0
sp=0
for i in k:
    if(i==1):
        fp=fp+1
    if(i==2):
        sp=sp+1
print "First Player %s" %fp
print "Second Player %s" %sp


