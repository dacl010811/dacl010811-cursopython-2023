


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

division()
    
