


# set()
conjunto = set() # {1,2,4,14,4}

# Metodos add
conjunto.add(1)
conjunto.add(10)
conjunto.add(100)
conjunto.add(1000)
conjunto.add(1)
conjunto.add(1000)
conjunto.add(1000000)        # [ 1, 2, 5, ]            ------->     0x5454FB11                       
print(conjunto)

# Metodos discard 
conjunto.discard(1)
conjunto.discard(10)
print(conjunto)               #------->     0x5454FB11  

# Metodos copiar 
conjunto2 = conjunto.copy()               #------->     0x54545454545   
print(conjunto2)

# Metodos clear()
conjunto.clear()

print(conjunto)
print(conjunto2)

# Creacion de Conjuntos  mediante {}
#c1 = {1,2,3}

c1 = {3,2,1}
c2 = {3,4,5}

c3 = {-1,99}
c4 = {1,2,3,4,5}

print(f"{c1.isdisjoint(c2)}")
print(f"{c1.isdisjoint(c3)}")
print(f"{c1.isdisjoint(c4)}")


print("--------- issubset --------")
print(f"{c1.issubset(c2)}")
print(f"{c1.issubset(c4)}")

print("--------- issuperset --------")
print(f"{c4.issuperset(c1)}")
print(f"{c4.issuperset(c2)}")
print(f"{c1.issuperset(c4)}")


# Metodos avanzados de conjuntos

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

print("Metodos Avanzados")
resultado_union = c1.union(c2)
print(resultado_union)

if resultado_union == c4:
    print("Los conjuntos son iguales")
else:
    print("Los conjuntos NO son iguales")

print(resultado_union)

print("--------- UPdate en Conjuntos ---------")
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

print(f"Conjunto Original c1 : {c1}")
c1.update(c2)
print(f"Conjunto Final c1 : {c1}")

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

print("--------- difference en Conjuntos ---------")
conjunto_direfencias = c1.difference(c2)
conjunto_direfencias_1 = c2.difference(c1)

print(conjunto_direfencias)
print(conjunto_direfencias_1)

print("--------- difference en Conjuntos ---------")
print(f"Original : {c2}")
c2.difference_update(c1)
print(f"Resultado Final : {c2}")


print("Interseccion de Conjuntos")
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

conjunto_interseccion = c1.intersection(c2)
print(f"{conjunto_interseccion}")

conjunto_interseccion_1 = c1.intersection(c4)
print(f"{conjunto_interseccion_1}")

c4.intersection_update(c1)
print(f"{c1}")


print("Diferencia Simetrica de Conjuntos")
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

conj_1 =  c1.symmetric_difference(c4)
print(conj_1)

print(f"Original {c2}")
c2.symmetric_difference_update(c4)
print(f"Resultado Final {c2}")










