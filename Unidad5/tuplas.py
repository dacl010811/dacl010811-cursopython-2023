


#  se las representa  por () y son inmutables
#  Contener cualquier tipo de dato de tipo simple : String, boolean, int, float etc

my_tupla = (2,4.9,"Hola Mundo", True)

#Indexacion de las tuplas
# Indices son la posiscion donde se encuentra el dato almacenado
# Los indeices se enumeran desde 0

my_tupla = (2, 4.9,"Hola Mundo", True)
           #0   1        2         3     4   5       6 
           
print(my_tupla[0])
print(my_tupla[3])
print(my_tupla[1])
print(my_tupla[2])

# Slicing : [indice Inicial : Indice Final]

print("----------SLICING------------")

my_tupla = (2, 4.9,"Hola Mundo", True)
           #0   1        2         3     4   5       6 
           # -4   -3    -2        -1 
           
print(my_tupla[1:3]) # Slicing con indice inicial y indice final (n-1)
print(my_tupla[1:4]) # Slicing con indice inicial y indice final (n-1)
print(my_tupla[1:]) # Slicing con indice inicial y indice 
print(my_tupla[:]) # Slicing con indice inicial y indice 

print("--------- SLICING NEGATIVOS-------------")

my_tupla = (2, 4.9,"Hola Mundo", True)
           #0   1        2         3     4   5       6 
           # -4   -3    -2        -1 

my_tupla_2 = (21,)
print(my_tupla_2)
print(type(my_tupla_2))

my_tupla = (2, 4.9,"Hola Mundo", True)
           #0   1        2         3     4   5       6 
           # -4   -3    -2        -1 

print(my_tupla[:-1]) # Slicing con indice inicial y indice
print(my_tupla[1:-2]) # Slicing con indice inicial y indice

print(my_tupla)

#Tuplas son inmutables

my_tupla = (2, 4.9,"Hola Mundo", True, [1, 2, 3, 4, 5])
#my_tupla[10] = 100
print(my_tupla) # Inmutables 

my_tupla = (2, 4.9,"Hola Mundo", True, [1, 250, 300, 49, 5])


print('--------- Operacion longitud --------')
print(len(my_tupla[4]))
print(my_tupla[4][1])
print(my_tupla[-1][3])

my_tupla = (2.1, 4.9,"Hola Mundo", True,2,[1, 250, 300, 49, 5],2,[])
print(f" Existen tantos elementos : {my_tupla.count([])}")

# index() --> Me da el indice de  la primera ocurrencia del dato a buscar

my_tupla = (2.1,4.9,"Hola Mundo", True,[1, 250, 300, 49, 5],2,[],False, True,200)

#print (f"El indice que buscas esta en index : {my_tupla.index(2000000)}")

#Carcateristica de Inmutabilidad
print("---- INMUTABLES------")
my_tupla = (2.1,4.9,"Hola Mundo", True,[1, 250, 300, 49, 5],2,[],False, True,200)
#my_tupla.append("Darwin")

print(my_tupla)


 









           

