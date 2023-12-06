




# Para definir un conjunto tenermos 2 formas:
# set()---->  Clase de python
# {1,2,3}  --- Literal de tipo conjunto 
# {2.0,3.0,4.0,4.0} --- Utilizar un mismo tipo de dato

conjunto = set((1,2,3,2,2,2,2,2,4,5,6,7))
print(conjunto)

conjunto = set()
conjunto.add(8)
conjunto.add(6)
conjunto.add(4)

conjunto.add(6)
conjunto.add(6)
conjunto.add(6)

print(conjunto)

print("Eliminar")
conjunto.remove(4)
print(conjunto)
#conjunto.remove(4)

#

conjunto.add(8)
conjunto.add(6)
conjunto.add(4)

conjunto.update([50,78,78,877,777])
conjunto.update([2,14])
conjunto.update([2,16])

print(conjunto)


# Creando conjunto a partir de una lista

lista = [1,2,3,4,5,6,7,8,9,10,3,4,5]

conjunto = set(lista)
print(conjunto)


# Proceso inverso es convertir el conjunto a lista


conjunto = { "Mensaje1", 10, 10.25, "Mensaje2", True}

print('Transformando')
aux = list(conjunto)
print(type(aux))
print(aux)


#  Transformar las cadenas a Conjunto

mensaje = "Hola Mundo, python"

conjunto_letras = set(mensaje)
print(type(conjunto_letras))
print(conjunto_letras)

conjunto_1 = {}











