text = "cau"
text2 = ' ahoj'
print(text)

text3 = "bo/mba"
print(text3)

print(text+text2)
print(text2*3)

var = "Ahoj Karle"
print(var[6]) #indexovani od 0!!!
print(len(var))

print(var[5:10]) #print( slice interval <5;10) )
print(var[5:10:2])
print(var[5:10:-2])
print(var[5:])
print(var[:5])
print(var[:4:-1])
print(var[::-1])
print(var.index("j"))

for i in range(len(var)): #print(var[len(var)-1]) lze nahradit print(var[-1])
    print(var[i])

for i in range(len(var)): #for i in range(len(var)) lze nahradit for i in var
    print(var[-i-1])

for i in range(len(var)):
    print(var[:i+1])

for i in range(len(var)-1):
    print(var[i:i+2:])

for i in range(len(var)-2):
    print(var[i:i+3:])

for i in range(int(len(var)/2)+1):
    print(var[i],var[-i-1])