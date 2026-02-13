def dis(a,b,c):
    d = b**2 - 4*a*c
    if (d < 0):
        return "n.r."
    elif (d == 0):
        x = -b / 2 * a
        return x
    else:
        x1 = (-b + D**(1/2))/(2*a)
        x2 = (-b - D ** (1 / 2)) / (2 * a)
        return x1, x2

def quad(a,b,c):
    vysledek = ((-b)+(dis(1,2,1)**1/2))/2*a + 0*c
    return vysledek

print(dis(1,2,1))
print(quad(1, 2, 1))