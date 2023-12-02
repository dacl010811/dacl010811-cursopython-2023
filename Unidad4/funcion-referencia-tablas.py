



# FUnciones por Referencias
# Referencias, vamos a pasar a  las funciones tipos de  datos completos:  [] , () y  {}

#LIsta
lista =  [4,6,8,10]  #  Resultado [4**3,6**3,8**3,10**3] --->  Direccion de Memora --> 0x4587ADF
         #0 1  2  3 indices   

def  potencia_3 (lista):
              
    for index, valor in enumerate(lista):   #  Indices, Valor
        lista[index] = valor**3    
    print ("Lista Interna: {0}".format(lista))
    

print("La lista antes de la invocacion por referncia:  {0} ".format(lista)) # Lista Original

potencia_3(lista[:]) # --->  Direccion de Memora --> 0x4587ADF87

print("La lista despues de la invocacion por referencia:  {0} ".format(lista)) # Lista Original





