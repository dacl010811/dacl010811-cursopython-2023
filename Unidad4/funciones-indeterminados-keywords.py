


# Para definir un direccionario lo hacemos asi:  
# Direccionario se compone de multiples "clave:valor" , "clave:valor"

diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "pais": "Colombia"
}

print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["pais"])
print(diccionario['edad'])

# Funciones indeterminadas con la expresion "**kwargs"

def  mostrar_elementos_indeterminados(**kwargs):
    for key, value in kwargs.items():
        print(f"key [{key}] ----> [{value}] ")
        

mostrar_elementos_indeterminados(nombre="Juan",edad=25,pais="Colombia") # **kwargs



# Funciones integradas en python

numero_base_10 = 10
print (bin(numero_base_10))
print (hex(numero_base_10))

print(int('0b1010',2))
print(int('0xa',16))

print(abs(+8.52))
valor =  52.89565656565656565
print (f"{valor:.5f}")
print(round(5.99))

print("----------------")
print(eval('5**3'))

print(f"len= {len([1,3,1,'Mensaje',True])}")
print(len("Darwin"))

help()

