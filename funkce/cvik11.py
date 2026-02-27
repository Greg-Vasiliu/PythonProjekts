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

def prvo (cislo):
    if cislo < 2:
        return False
    for i in range(2,cislo+1):
        if cislo % i == 0:
            return False
    return True


print(prvo(13))
