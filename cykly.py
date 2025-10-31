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
for i in range(len(var)): #print(var[len(var)-1]) rovna se print(var[-1])
    print(var[i])

print(var[5:10]) #print( slice interval <5;10) )
print(var[5:10:2])
print(var[5:10:-2])
print(var[5:])
print(var[:5])
print(var[:4:-1])
print(var[::-1])
print(var.index("j"))