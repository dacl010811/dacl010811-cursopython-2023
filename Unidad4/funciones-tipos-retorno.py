

def suma(a,b):
    return a + b
resultado = suma(0,0.0000000e12)
print(type(resultado))
print(resultado)


def potenciacion(a,b,c):
    a = a ** 2   #  3**2 = 9
    b = b ** 2   #  2**2 = 4
    c = c ** 2   #  7**2 = 49    
    return  a,b,c # Python entiendo q esto es una tupla

# Defincion de variables multiples por posicion
x,y,z = potenciacion(3,2,7)

print("Variable X: {0} ".format(x))
print("Variable Y: {0}".format(y))
print("Variable z: {0}".format(z))


