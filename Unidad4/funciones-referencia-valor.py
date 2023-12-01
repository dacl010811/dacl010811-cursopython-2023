
# EL paso de argumentos a funciones  por valor
# Tipos de datos simples :  int, float, boolean y string

def suma(a,b):
    return a + b

resultado = suma(15,25)
#print (resultado)

# Envio de argumentos a la funcion por referencia: 
# POr referencia significa que python accede a los objetos: listas, tuplas
# diccionarios por una direccion en la memoria: 0x078AB ---> [1,2,3]

def multiplos_100(lista_numeros):
    for i,v in enumerate(lista_numeros):
        print(i,"-",v)
        lista_numeros [i] = v * 100
                
lista_numeros = [2,4,6]  # Listas, Tuplas, Diccionarios, Pilas y Colas
               # 0 1 2
print("Antes de : {0}".format(lista_numeros))
multiplos_100(lista_numeros)  
print("Despues de : {0}".format(lista_numeros))

