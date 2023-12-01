

# Argumentos por poscion
# Argumentos por nombre
# Argumentos por defecto
# funciones con argumentos indeterminados:  *args

def suma(a,b,c,d,e,f,g,h,i,j):
    return a + b  + c + d + e + f + g + h + i + j

resultado = suma(1,2,3,4,5,6,7,8,9,10)
#print("El resultado es = {0}".format(resultado))

# Mejorando el codigo

def suma_mejorada(*args):  # "*args" --> Representa un conjunto de datos, que es un tupla:  my_tupla = (1,2,3,4)
    sumatoria = 0    
    for dato in args:
        sumatoria += dato    
    return sumatoria

resultado_1 = suma_mejorada(5,4,34,5,18,56)
print(f"El resultado es = {resultado_1}")



