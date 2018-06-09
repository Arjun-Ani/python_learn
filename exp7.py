conv=lambda a,b:a>=b and int(a)+1.0 or int(a)
a=raw_input("Enter the number\n")
b=float(int(float(a))+0.5)
print conv(float(a),b)
