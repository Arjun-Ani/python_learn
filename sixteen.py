import random
a=raw_input("Enter the range\n")
chars='qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+-{}[]?/>.<,TYUIOPASDFGHJKLZXCVBNM;'
i=0
passwd=""
while(i<int(a)):
    passwd=passwd+random.choice(chars)
    i=i+1
print passwd

