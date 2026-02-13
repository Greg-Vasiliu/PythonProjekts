def scitani (a, b): #define func name, used data types, actual code, returned value
    reseni = a + b #every def has fresh var names, dw abt using "a" again
    return reseni

x = 5
y = 10
vysledek = scitani(x,y)
print(vysledek)

def napis_ahoj():
    print("ahoj")

var = napis_ahoj()
print(var) #napis_ has undefined return => value = None

