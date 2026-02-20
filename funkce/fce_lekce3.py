import numpy as np
# def secti(a,b):
#     return a+b
# def vypis_soucet(a,b):
#     print(a+b)
# print(secti(2,3))
# print("*********")
# print(vypis_soucet(2,3)) #vypis_ returns None, print() is obsolete (print() also returns None)

# def secti(a,b):
#     return a+b
# def odecti(a,b):
#     return a-b
# def vynasob_soucet_a_rozdil(a,b,c,d):
#     soucet = secti(a,b)
#     rozdil = odecti(c,d)
#     return soucet * rozdil
# vysledek=vynasob_soucet_a_rozdil(1,2,5,3)
# print("Vysledek (a+b)*(c-d)=" + str(vysledek))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# def odpocet(n):
#     if n <=0:
#         print("boom")
#         return
#     else:
#         print("T-"+str(n))
#         odpocet(n-1)
# odpocet(5)

def soucet(n):
    if n<=1:
        return 1
    else: #in case of D6, sum of all face values is 21
        return n + soucet(n-1)
print(soucet(6))
