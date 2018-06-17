import datetime
current = datetime.datetime.now()
#print current.year
name=raw_input("Enter your name\n")
#print name
age=raw_input("Enter your age\n")
#print age
diff=100-int(age)
#print diff
result=diff+current.year
times=raw_input("Enter the number of times the output should be displayed\n")
#print times
i=0
while(i<int(times)):
	print "%s)In %s you will be of 100 years age" %(i+1,result)
	i=int(i)+1


