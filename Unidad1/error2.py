mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Lista de claves a eliminar
claves_a_eliminar = ['a', 'c']

# Iterar sobre las claves y eliminar utilizando del
for clave in claves_a_eliminar:
    if clave in mi_diccionario:
        del mi_diccionario[clave]

# Mostrar el diccionario resultante
print("Diccionario después de eliminar elementos:", mi_diccionario)

# Mostrar el número de items restantes en el diccionario
num_items = len(mi_diccionario)
print("Número de items restantes en el diccionario:", num_items)
