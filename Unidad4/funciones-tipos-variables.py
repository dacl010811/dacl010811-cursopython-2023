
nombre_1 = "Nicolas"      #Variables globales :  Deben ser referenciadas antes de la DEFINICION de
                          # funcion

def saludo():
    #nombre_1 = "Darwin"   # Variables locales
    nombre_2 = "Augusto"  # Variables locales
    apellido_1 = "Calle"   # Variables locales
    apellido_2 = "Cañar"  # Variables locales
    
    print("Hola, bienvenido {0} {1} {2} {3}".format(nombre_1,nombre_2,apellido_1,apellido_2)) 
    
nombre_1 = "Elena"        # Las variables globales pueden ser definidas antes de la INVOCACION  de la funcion
saludo()

#nombre_1 = "Elena"