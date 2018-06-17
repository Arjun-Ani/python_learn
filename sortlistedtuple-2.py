a=input("Enter the Limit\n")
b=[(raw_input("Enter the name\n"),input("Enter the age\n"),input("Enter the score\n")) for i in range(a)]
print sorted(b)
