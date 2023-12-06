


diccionario_1 = {
    "nombre" : "Darwin",
    "edad" : 35.5,
    "cedula" : 11085258525,
    "telefono" : "0999558744",
    "3" : 15
}

diccionario_1["cuidad"] = "Quito"
print(diccionario_1)

#Conversion de listas a diccionarios

lista_llaves = ["a","b","c"]
lista_datos = ["100","200","3000"]
 
dic_2  =  dict(zip(lista_llaves,lista_datos))

print(dic_2)
