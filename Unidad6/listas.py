


# Metodos utilizados en listas
lista_datos = [2,3,4,True,[34,45,100],False,12.5,89,(3.1416,)]

#Metodo  append()
lista_datos.append(["A","B","C"])
print(lista_datos)

#Metodo  clear()
lista_datos.clear()
print(lista_datos)

#Metodo  append()
lista_datos.append(["A","B","C"])
print(lista_datos)

#Metodo  extend()
lista1 = [1,2,3,4,True, True, [25,50], False]
lista_datos.extend([(lista1,)])
print(lista_datos)

#Metodo  count()
lista1 = [1,2,3,4,True, True, [25,50], False]
print(f"Encontre  {lista1.count(True)} elementos iguales con el patron 'True'")

#Metodo  index()
lista1 = [ 1, 40, [25,50], False]
         # 0  1      2       3
print(f"Se encuentra en la posicion: [{lista1.index(40)}] ")

#Metodo  insert()
lista1 = [ 1, 40,         [25,50], False]
         # 0  1      2       3       4
         
print(f"Lista Original: {lista1} ")
lista1.insert(2, "Darwin Calle")        
print(f" Insert : {lista1}")

print(f"Lista Original: {lista1} ")
lista1.insert(2, "Nicolas")        
print(f" Insert : {lista1}")

# pop() y pop(5) en listas

print("-------------POPS --------------------")

lista1 = [ 1, 40, [25,50], False]
        #  0   1     2       3
print(f"Lista Original: {lista1} ")
lista1.pop()
print(f"Lista despues de pop: {lista1} ")

print(f"Lista Original: {lista1} ")
lista1.pop(1)

print(f"Lista despues de pop con index: {lista1} ")

print("-------- REMOVE --------")
lista1.remove(1)
print(f"Lista final {lista1} ")
#del lista1[2]


lista2 = [1,3,5,7,9,0]  #  [0,9,7,5,3,1]
print(f"Lista final reverse : {lista2.reverse()}")