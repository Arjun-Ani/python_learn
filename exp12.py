b=map(lambda x:[i for i in str(x) if int(i)%2==0  ],[x for x in range(1000,3001)])
c=[i for i in b if len(i)==4]
d=[]
for i in c:
    a=''.join(str(e) for e in i)
    d.append(a)
print d
