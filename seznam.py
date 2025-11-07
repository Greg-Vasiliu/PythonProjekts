
p2 = [1, "abc", 5.5, True, [1, 2, "a"]]
print (p2)
print (type(p2))
print ()

x = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(x)):
    if i%2 == 0:
        print(x[i])

for i in range(0, len(x), 2):
    print (x[i])