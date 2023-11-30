



# Crear funcion potencia


#Posicionalmente, se debe respetar el orden como fue definida la funcion con sus parametros
def potencia(b,e):
    return b**e

resp = potencia(2,3)
print(f"Potencia 1 :  {resp}")

# LLamada a la funcion por argumentos x nombre

resultado_potencia = potencia(e=3,b=2)
print(f"Potencia 2 :  {resultado_potencia}")

# Funciones con argumentos por defecto

def saludo (nombre="XYZ"):
    print(f"Seas bienvenido al curso de python: {nombre}")
    
    
# La primera es cuando le envio el argumento "nombre"

#saludo(nombre="Jose María")

#saludo()

#saludo()


# Programa de suma con argumentos por defecto

def suma(a,b,c):
    return  a + b + c

def suma_1(a=0,b=0,c=0):
    return  a + b + c


res_1 = suma(10,20,30)

res_2 = suma_1()

print(f"Respuesta 1 : {res_1}")
print(f"Respuesta 2 : {res_2}")



