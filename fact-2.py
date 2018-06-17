a=raw_input("Enter the Number\n")
fact=lambda x:x and x*fact(x-1) or 1
print fact(int(a))
