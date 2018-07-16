import re
a=raw_input("Enter the passwprd\n")
digit=0
letter=0
caps=0
special=0
res=0
for i in a:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
    elif i.isupper():
        caps=caps+1

if(len(a)>6 and len(a)<12):
    res=res+1
elif re.search("[$#@]",a):
    res=res+1
elif digit==0 and letter==0 and caps==0:
    res=res+1

if res==0:
    print "Please satisfy the condition"
else:
    print "password correct"
