import numpy as np

# lis = [99,1,3,2,5,4,7,6,9,8,10]
#
# def druhe (vstup):
#     if vstup[0] > vstup[1]:
#         max = vstup[0]
#         scd = vstup[1]
#     else:
#         max = vstup[1]
#         scd = vstup[0]
#
#     for i in range(1,len(vstup)):
#         if vstup[i] > max:
#             scd = max
#             max = vstup[i]
#         elif vstup[i] > scd:
#             scd = vstup[i]
#     return scd
#
# print(druhe(lis))

# def prvo (cislo):
#     if cislo < 2:
#         return False
#     for i in range(2,cislo):
#         if cislo % i == 0:
#             return False
#     return True


# print(prvo(13))

# def count_prvo (seznam):
#     pocitadlo = 0
#     for i in range(len(seznam)):
#         if prvo(seznam[i]):
#             pocitadlo+=1
#     return pocitadlo
#
# print (count_prvo([1,5,13,25,16,7]))

# def fce_add(a,b,c=10,d=10): #input overrides c & d defaults
#     return a+b+c+d
# print(fce_add(1,2))
# print(fce_add(1,2,3)) #if each param has default, order don't matter

def fukce_add(*args):
    print(args)
    soucet=0
    for i in range(len(args)):
        soucet +=args[i]
    return soucet

print(fukce_add(1,2,3,4))
print(fukce_add(1,2))