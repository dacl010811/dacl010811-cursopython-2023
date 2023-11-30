

#Caracteristicas:
# Para definir la funcione en python utilizamos la pala
# reservada :  "def" 

# Definiendo o creando funciones en python
def suma(x, y):
    return x + y

def resta(a, b):
    return a - b

def multiplicacion(c, d):
    return  c * d

def division(e, f):
    return e / f

def saludo():
    print('Saludo desde Python!!')    
    print("Es un print que si pertenece a ninguna funcion!!")
    
# Invocar funciones en python
#saludo()

# Invocar a la funcion 'suma()'

x = 10.9
y = 8.1

respuesta =  suma(x,y)
print(f" La sumatoria de {x} + {y} = {respuesta}")

# Invocar a la funcion 'resta()'
a = 500
b = 350
respuesta_r = resta(a,b)
print(f" La resta de:  {a} - {b} = {respuesta_r}")


# Invocar a la funcion 'multiplicacion()'

c1 = 100
c3 = 200
respuesta_mul = multiplicacion(c1,c3)


print(f"La respuesta de la multiplicacion = {respuesta_mul}")
