
# p2 = [1, "abc", 5.5, True, [1, 2, "a"]]
# print (p2)
# print (type(p2))
# print ()

# x = [1, 2, 3, 4, 5, 6, 7, 8]

# print(x)
# print(type(x))
# print(x[1:4])

# for i in range(len(x)):
#     if i%2 == 0:
#         print(x[i])

# for i in range(0, len(x), 2): # (floor, ceiling, step)
#     print (x[i])
#
# pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

# max_prvek = pole [0] #pomocne promenne pro logickou strukturu
# pos_max_prvek = 0

# for i in range(1, len(pole)):
#     if max_prvek < pole[i]:
#         max_prvek = pole[i]
#         pos_max_prvek = i
# print(f'{max_prvek} je maximalni prvek a je na pozici {pos_max_prvek}')

# for i in range(1, len(pole)):
#     if max_prvek > pole[i]:
#         max_prvek = pole[i]
#         pos_max_prvek = i
# print(f'{max_prvek} je minimalni prvek a je na pozici {pos_max_prvek}')

# prum = 0
#
# for i in pole:
#     prum = prum+i #to same jako prum += pole[i]
#
#print(prum/len(pole))

# counter = 0
# limit = 5
# for i in range(len(pole)):
#     if pole[i] > limit:
#         counter+= 1
#print("Pocet prvku vetsich nez "+str(limit)+" je: "+str(counter))

# souc = 0

# for i in pole:
#     souc = souc+i

# print(prum)
pole = [5, 2, 9, 1, 7, 3, 1, 6, 4]
nove_pole =[]

for i in range(len(pole)-1, -1, -1): #len = 9, zacneme (9-1); chceme pos0, => interval edge = -1; krok -1
    nove_pole.append(pole[i])
print(nove_pole)