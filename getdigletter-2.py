a=raw_input("Enter the sentence\n")
digit=0
letter=0
for i in a:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
    else:
        pass
print "DIGIT=%s" %digit
print "LETTER=%s" %letter

