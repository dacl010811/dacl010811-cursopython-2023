

# Para trabajar con ficheros o archivos en python debo importar el metodo open()
from io import open
import time

def crear_archivo(nombre="default.txt"):
    
    archivo = open(nombre,"w")
    
    bandera = 1
    while bandera != 0:
        respuesta_usuario = input("Deseas escribir en el archivo, y/n \n")    
        if respuesta_usuario == 'y':
            mensaje = input("Ingresa el mensaje : \n")
            archivo.write(mensaje+"\n")
        else:
            archivo.close()
            break
        
#crear_archivo()
def leer_archivo(nombre):
    conetenido=""
    try:
        fichero = open(nombre, "r")
        conetenido = fichero.read()    
    except FileNotFoundError as fn:
        print(f"FileNotFoundError: Error al  ubicar el archivo : {nombre}")
    except Exception as ex: 
        print(f"Error general al leer el archivo: {nombre}: error : {type(ex).__name__}")    
    return conetenido

#print(f"El contenido del archivo es : \n {leer_archivo('default.txt')}")
        
def leer_archivo_lista(nombre):
    lista_strings=""
    try:
        fichero = open(nombre, "r")
        lista_strings = fichero.readlines()   
    except FileNotFoundError as fn:
        print(f"FileNotFoundError: Error al  ubicar el archivo : {nombre}")
    except Exception as ex: 
        print(f"Error general al leer el archivo: {nombre}: error : {type(ex).__name__}")    
    return lista_strings


#lista_contenido = leer_archivo_lista('default11.txt')

#if len(lista_contenido) > 0:
#    contador = 0
#    for linea in lista_contenido:
#        contador += 1
#        print(f" Linea {contador} :  {linea}")
#        time.sleep(0.25)

def escribir_archivo_append(nombre, mensaje):
    
    try:
        fichero = open(nombre, "a")
        if mensaje != None:
            fichero.write(mensaje+"\n")
    except FileNotFoundError as fn:
        print(f"FileNotFoundError: Error al  ubicar el archivo : {nombre}")
    except Exception as ex: 
        print(f"Error general al leer el archivo: {nombre}: error : {type(ex).__name__}")         
    finally:
        fichero.close()


escribir_archivo_append("default.txt", "")
