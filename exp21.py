import math
b=[]
a=raw_input("Enter the step of the roboti\n")
b.append(a)
while a:
    a=raw_input("Enter the step of the robot\n")
    if a!="\n":
        b.append(a)
c=[i.split(' ') for i in b]
up=0
left=0
for i in c:
    if i[0]=="up":
        up=up+int(i[1])
    elif i[0]=="down":
        up=up-int(i[1])
    elif i[0]=="right":
        left=left+int(i[1])
    elif i[0]=="left":
        left=left-int(i[1])

dist=int(math.sqrt((up**2)+(left**2)))
print "distance=%s" %dist
