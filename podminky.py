vstup = input("Zadej cislo: ")
try:
    cislo = int(vstup)
except:
    cislo = 0
print("vstup = " + vstup)

if cislo > 5:
    print("vetsi")
elif cislo > 3:
    print("neco")
else:
    print("neni vetsi")
print("konec")

a = input("zadej A")
b = input("zadej B")
c = input("zadej C")

# AX^2 + BX + C = 0
d = b**2 - 4*a*c
if a == 0:
    print("nula reseni v R")
elif d > 0:
    print("dve reseni v R")
elif d == 0:
    print("jedno reseni v R")
else:
    print("nula reseni v R")