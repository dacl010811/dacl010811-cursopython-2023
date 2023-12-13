


#Errores semanticos


def  eliminarElementos():
    lista = [1,2,3,4,5]

    while  len(lista) > 0:
        if len(lista) >= 0:
            lista.pop()
            print(len(lista))
    else:
        print("NO hay elementos por eliminar,  la lista està vacia")

def  division():
    bandera = int(input("Deseas continuar presiona 1 \n"))
    while bandera == 1:
        try:    
            dividendo = float(input("Ingresa un numero para la division: \n"))
            divisor = float(input("Ingresa un numero para la division: \n"))
            respuesta =  dividendo / divisor
            print(f"La respuesta de dividir {dividendo}/{divisor} = {respuesta}")
        except ZeroDivisionError as ve:
            print(f"Controlando ZeroDivisionError --> {type(ve).__name__}")
        except ValueError as ve:
            print(f"Controlando ValueError --> {type(ve).__name__}")
        except Exception as error:
            print(f"Error General, verifica los datos de entrada")
        else:
            print("Todo funciona sin novedades")
        
        bandera = int(input(" Deseas continuar presiona 1, sino (0) para salir \n"))
        if bandera != 1:
            break

    print("Finalizo el programa!!")

def  divisionFinally():
    
    valor_1 = input("Ingrese un valor 1: \n")
    valor_2 = input("Ingrese un valor 2: \n")
    
    try:
        resultado = valor_1 / valor_2
    except TypeError as error:
        print(f"Error de Tipo : {type(error)}")    
    except Exception as error:
        print(f"Excepcion General : {type(error)}")
    else:
        print("Funciono correctamente y entro al else")
    finally:
        print("Siempre pasaré por aqui!!!")
        resultado = 0
        try:
            valor_1 = float(valor_1)
            valor_2 = float(valor_2)
            resultado = valor_1 / valor_2
        except ValueError as ve:
            print(f"Error interno finally: {type(ve)}")
        except UnboundLocalError as ve:
            print(f"Error UnboundLocalError finally: {type(ve)}")
            resultado = 0
        except  Exception as error:
            print(f"Error General interno finally: {type(error)}")
        
        print(f"El resultado es : {resultado}")
    
#divisionFinally()

# La instrucción raise

def presentarMensaje(mensaje=None):
    try:
        if mensaje is None:
            raise  ValueError   
    except ValueError as ve:
        print(f"LLamado por raise: {type(ve).__name__}")
    except ZeroDivisionError as ve:
        print(f"LLamado por raise: {type(ve).__name__}")
    except TypeError as ve:
        print(f"LLamado por raise: {type(ve).__name__}")
    except:
        print(f"Error General")
    else:
        print(f"El flujo fue normal, sin excepciones!!!")
    finally:
        print(f" Soy finally : Darwin : {mensaje}")

presentarMensaje()
presentarMensaje("Bienvenido")
