import pickle
from io import open



def crear_archivo_binario(nombre, datos):    
    
    try:
        archivo = open(nombre, 'wb')
        pickle.dump(datos,archivo)
    except Exception as er:
        print(f"Error General : {type(er)}")
        archivo.close()
    finally:
        archivo.close()
        
#mis_claves = {"clave-hotmail":"1234","clave-gmail":"6789"}
#crear_archivo_binario("vault",mis_claves)
    

def  leer_archivo_binario(nombre):
    try:
        archivo = open(nombre, 'rb')
        passwords = pickle.load(archivo)
    except Exception as er:
        print(f"Error General : {type(er)}")
        archivo.close()
    finally:
        archivo.close()
    return passwords
        
print(f" Estas son tus claves desencriptadas : \n {leer_archivo_binario('vault')}")
