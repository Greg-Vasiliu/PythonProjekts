
def secti(a,b):
    vysledek = a+b+globalni_promenna #as long as all codeVars are def'd before 1st use of func, varDef can go after
    return vysledek

globalni_promenna = 10 #varDef outside the func code overrides the inside

def go(a,b):
    #globalni_promenna = 99
    vysledek = a+b+globalni_promenna
    return vysledek

# y = go(5,3)
# print(y)

def secti_tuple(a,b): #octuple. a kinda list, cannot be assigned value
    globalni_promenna = 20
    vysledek = a+b+globalni_promenna
    return vysledek, globalni_promenna

y = secti(5,3)
print(y)
print(type(y))
print(secti_tuple(5,3))
print(type(secti_tuple(5,3)))

