# jmeno = input("zadej jmeno: ")
#
# print("Uzivatel zadal "+jmeno)
#
# cislo = input("zadej cislo: ")
#
# print("Uzivatel zadal "+cislo) #output is only string (because user inputs string [keyboard])

#priklad hesla

# heslo = input("Zadej heslo: ")
# skutecne_heslo = "heslo123"
#
# if heslo == skutecne_heslo:
#     print("logged in")
# else:
#     print("incorrect")

#priklad input integer

# cislo_txt = input("zadej cislo: ")
# cislo_real = int(cislo_txt)#converting back to string in case input is letters instead of digits
# print("zadane cislo + 10 = " + str(cislo_real + 10)) #or just use "try: except:"

#priklad ask input until correct type
# while True:
#     cislo_txt = input("napis cislo: ")
#     try:
#         cislo = int(cislo_txt)
#         break
#     except:
#         pass
# print("spravne")

import numpy as np #brief

# for i in range(10):
#     cislo = np.random.randint(10,20) #interval is <_;_) with default low = 0.,program adds hints "low/high"
#     rnd = np.random.random() #default interval <0;1)
#     print(cislo)
#     print(rnd)

jo = np.random.randint(1,21)
for i in range(21):
    cislo_txt=input("odhadni cislo: ")
    try:
        cislo=int(cislo_txt)
        if (cislo == jo):
            print("spravne")
            break
        elif (cislo > jo):
            print("mensi")
        elif (cislo < jo):
            print("vetsi")
    except:
        print("neni cislo")