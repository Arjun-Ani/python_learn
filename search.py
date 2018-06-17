def list_input(n):
    i=0
    ip=[]
    while(i<n):
        a=raw_input("Enter your input\n")
        ip.append(int(a))
        i=i+1
    return ip

def list_search(li,no):
    g=0
    for i in li:
        if(no==i):
            g=g+1
    if(g==0):
        return False
    else:
        return True
n=raw_input("Enter the size of the list\n")
ip=list_input(int(n))
ip.sort()
k=raw_input("Enter the number to be searched\n")
t=list_search(ip,int(k))
print t

