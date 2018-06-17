b=input("Enter the limit\n")
a=map(lambda x: x%2!=0 and x**2,[input("Enter the number\n") for i in range(b)])
print a
