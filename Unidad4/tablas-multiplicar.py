#   2  * 1 ....... 
#   2  * 2 .....
#   2 * 12 = 24

def ingreso_datos_usuario():
    datos  = [] # Lista
     
    numero_tabla = int(input("Ingresa el # tabla que deseas!! \n"))
    datos.append(numero_tabla)
    
    limite = int(input("Ingresa el limite que deseas!! \n"))
    datos.append(limite)
    
    return datos     # datos = [numero_tabla, limite]
                             #        [0]       [1]
   
def  tablas_multiplicacion (numero_tabla, limite=13 ):
    
    if limite != 13:
        limite += 1
            
    for numero in range(1,limite):
        print(f"{numero_tabla} * {numero} = {numero_tabla*numero}")
            
    
lista_datos = ingreso_datos_usuario()

tablas_multiplicacion(lista_datos[0], lista_datos[1])
tablas_multiplicacion(lista_datos[0])
    
        
#Invocacion 1:
#tablas_multiplicacion(5,limite=20)

# Invocacion 2:  Con argumento por defecto
#tablas_multiplicacion(8)

# Invocacion 3:  Con argumento por nombres
#tablas_multiplicacion(limite=5, numero_tabla=3)



