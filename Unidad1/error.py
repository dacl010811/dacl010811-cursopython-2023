


diccionario = {
    "nombre":"Darwin",
    "apellido":"Calle",
    "edad":40,
    "nacionalidad":"Ecuatoriana",
    "sexo":"masculino"
}


try:
    for key,dato in diccionario.items():
        if key in diccionario:
            print(f"Va a eleminar el dato: {dato}")
            del diccionario[key]
except Exception as er:
    print(er.__cause__)
else: 
    print("Else : ".format(diccionario.items()))
    
print(f"Diccionario tiene {len(diccionario)} elementos")
print(f"Diccionario tiene {diccionario} elementos")
    