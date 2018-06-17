import sys
def list_enter(a,d):
    b=raw_input("Enter the row(0-2)\n")
    c=raw_input("Enter the column(0-2)\n")
    if a[int(b)][int(c)]==0:
        a[int(b)][int(c)]=d
        for i in range(0,3):
            q=0
            p=0
            for j in range(0,3):
                if(a[i][j]==0):
                    p=1
                if(a[j][i]==0):
                    q=1
            if a[i][j]==a[i][j-1] and a[i][j]==a[i][j-2] and p==0:
                print "Winner %s" %a[i][j]
                sys.exit()
            if a[j][i]==a[j-1][i] and a[j][i]==a[j-2][i] and p==0:
                print "Winner %s" %a[i][j]
                sys.exit()
        if a[i][i]==a[i-1][i-1]==a[i-2][i-2]!=0:
            print "Winner %s" %a[i][j]
            sys.exit()
        if a[i-2][j]==a[i-1][j-1]==a[i][j-2]!=0:
            print "Winner %s" %a[i][j]
            sys.exit()
    else:
        print "Please select other row and column"
        list_enter(a,d)
    return a
def list_entry(a,i):
    print "First player's chance"
    a=list_enter(a,1)
    if(i<4):
        print "Second player's chance"
        a=list_enter(a,2)
    return a
a=[[0,0,0],[0,0,0],[0,0,0]]
i=0
k=[]
while(i<5):
    a=list_entry(a,i)
    i=i+1

