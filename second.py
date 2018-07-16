a=raw_input("Enter the devident\n")
b=raw_input("Enter the devisor\n")
if(float(a)%2==0):
	#print "%s is even" %a
	if(float(a)%4==0):
		print "%s is divisible with 2&4" %a
	else:
		print "%s is divisible by 2 but not with 4" %a
else:
	print "%s is odd" %a

if(float(a)%float(b)==0):
	print "%s is devisible by %s" %(a,b)
else:
	print "%s is not devisible by %s" %(a,b)

