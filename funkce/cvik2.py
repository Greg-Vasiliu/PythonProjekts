import random

#x = random.randint(10,20)

def hod_k6 ():
    #function description for mouse hover
    """
    Simuluje hod kostkou k6
    :return:
    int: nahodne cislo z intervalu 1 - 6 (vcetne)
    """
    return random.randint(1,6)

def pocet_pokusu_na_sestku ():
    a = 0
    x = hod_k6()
    if x == 6:
         return 1

    while x != 6 :
        x = hod_k6()
        #print("hodil",x)
        a += 1

    return a

#print(pocet_pokusu_na_sestku())


def simulace_pokusu (n):
    m = [0] * 20
    for i in range(n):
        x = pocet_pokusu_na_sestku()
        if x > 20:
            x = 20
        m[x - 1] += 1
    return m


print(simulace_pokusu(10000))


