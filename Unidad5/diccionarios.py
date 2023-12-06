


# Diccionarios, se componen principalmente del formato :     "key : value","key : value", "key : value", etc...

diccionario = {
    "nombre" : "Darwin",
    "edad" : 35.5,
    "cedula" : 11085258525,
    "telefone" : "0999558744",
    1 : 1,
    2 : 1000.52,
    "3" : 15
}

print(type(diccionario))
print(diccionario["3"])
print(diccionario)

# MOdificacion de datos en dicccionarios
print("--- MOdificando valores ------")
diccionario["edad"] = 40
diccionario["3"] = 1515151515.25
print(diccionario)

diccionario_1 = {
    "nombre" : "Darwin",
    "edad" : 35.5,
    "cedula" : 11085258525,
    "telefono" : "0999558744",
    "3" : 15
}

#Eliminar elementos de un diccionario

print("Eliminando datos del diccionario")
#del(diccionario_1["nombre"])
#del(diccionario_1["edad"])
#del(diccionario_1["telefone"])
#del(diccionario_1["3"])

print(f"tamaño diccionario: {len(diccionario_1)} ")

print(diccionario_1)

# Iterar el diccionario

for key in diccionario_1:
    print(f" K: {key}")
    print(f" Dato: {diccionario_1[key]}")
  
print(" Obtener unicamente los valores de los diccionarios")

for dato in diccionario_1.values():    
    print(f" Dato: {dato}")
    
print(" Otro For con items()")

for key,dato in diccionario_1.items():    
    print(f"  key : {key}   -   Dato: {dato}",end=" ")
    









