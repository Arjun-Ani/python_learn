max=lambda a,b:len(a)>len(b) and a or b
a=raw_input("Enter the first string\n")
b=raw_input("Enter the secong string\n")
print max(a,b)
