from io import open

def  leer_archivo_puntero(nombre):
    contenido = None
    try:
        archivo = open(nombre, "r")        
        if archivo != None:
            archivo.seek(len(archivo.readline()))
            #print(f"Ubicacion: {archivo.seek(10)} ")
            contenido = archivo.read(100)        
    except Exception as er:
        print(f"Excpecion General {type(er).__name__}")
  
    return contenido

#contenido = leer_archivo_puntero('miPrimerArchivo.txt')
#print(f"El contenido con seek() es : {contenido}")

import time
def leer_archivo_escritura_simultanea(nombre, mensajes):
    try:
        archivo = open(nombre, "r+")
        
        lineas = archivo.readlines()
        for linea in lineas:
            print(f"Linea [{linea}]")
            time.sleep(0.10)
        
        if mensajes != None:
            index = -1
            for linea in lineas:
                index +=1                
                if index % 2 == 0:
                   lineas [index] = mensajes
                   #archivo.write(mensajes+"\n")
            archivo.seek(0)
            archivo.writelines(lineas)
            
    except Exception as er:
        print(f"Error General : { type(er)}")
        archivo.close()
    else:
        archivo.close()
    finally:
        archivo.close()


leer_archivo_escritura_simultanea("default.txt","Hola Python 4.0")

