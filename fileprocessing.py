import os
a=open("Training_01.txt","r")
b=a.readlines()
c=len(b)
a.close()
for i in b:
    i=i.strip('\n')
    command="echo \"%s\" | awk -F\"/\" \'{print $3}\' >> output.txt" %i
    os.system(command)
nex="cat output.txt | uniq"
os.system(nex)
    



