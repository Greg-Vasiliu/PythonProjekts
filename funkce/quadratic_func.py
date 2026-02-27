def quad(a,b,c):
    d = b**2 - 4*a*c
    if (d < 0):
        return "n.r."
    elif (d == 0):
        x = -b / 2 * a
        return x
    else:
        x1 = (-b + d**(1/2))/(2*a)
        x2 = (-b - d ** (1 / 2)) / (2 * a)
        return [x1, x2]

def quad_test():
    results=[]
    for i in range(5):
        results.append(quad(1,i,1))
    return results

vysledky = quad_test()
for vysledek in vysledky:
    print(vysledek)