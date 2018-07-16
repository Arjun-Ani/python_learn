def sps():
    print "First Player"
    a=raw_input("Enter choice(stone/paper/scissor)\n")
    print "Second Player"
    b=raw_input("Enter choice(stone/paper/scissor)\n")
    if(a=="stone" and b=="paper"):
        print "player 2 wins"
    elif(a=="stone" and b=="scissor"):
        print "Player 1 wins"
    elif(a=="paper" and b=="scissor"):
        print "Player 2 wins"
    elif(a=="paper" and b=="rock"):
        print "player 1 wins"
    elif(a=="scissor" and b=="rock"):
        print "player 2 wins"
    else:
        print "player 1 wins"
c=raw_input("Enter the number of tries\n")
i=0
print c
while(i<int(c)):
    print i
    sps()
    i=i+1

