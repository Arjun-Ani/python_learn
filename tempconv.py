print "Temperature converter"
Ti=input("Enter a temperature:")
conv=lambda T,Ti:T=="F" and "Tf=%s" %(float(((9*Ti)/5)+32)) or  "Tc=%s" %(float(((5*Ti)/9)-32))
T=raw_input("Convert to (F)ahrenheit or (C)elsius?")
print conv(T,Ti)
