
def add(n1, n2):
    try:
        return n1 + n2
    except Exception as error :
        print (f"Error Exception: {error} :  {n1} {n2}")

def subtract(n1, n2):
    try:
        return n1 - n2
    except Exception as error :
        print (f"Error Exception: {error} :  {n1} {n2}")
    

def multiply(n1, n2):
    try:
        return n1 * n2
    except Exception as error :
        print (f"Error Exception: {error} :  {n1} {n2}")

def dividition(n1, n2):
                
    try:
        return n1 / n2
    except ZeroDivisionError as error :
        print (f"ValueError: {type(error).__name__}")
    except Exception as error :
        print (f"Error Exception: {error} :  {n1} {n2}")
 
 
def ingreso_teclado():
    n1 = float(input("Enter the first numer: \n"))
    n2 = float(input("Enter the second numer: \n")) 
    return n1,n2
    
def calculator():
    result = 0
    while True:
        print("select an option")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply ")
        print("4. Dividition")
                                        
        try:
            option = int(input("Enter the number of the operation you required: \n"))
            result = 0
            if option > 0:                                            
                if option == 1:
                    n1,n2 = ingreso_teclado()                    
                    result = add(n1, n2)
                elif option == 2:
                    n1,n2 = ingreso_teclado() 
                    result = subtract(n1, n2)
                elif option == 3:
                    n1,n2 = ingreso_teclado() 
                    result = multiply(n1,n2)
                elif option == 4:
                    n1,n2 = ingreso_teclado() 
                    result = dividition(n1, n2)
                else:
                    print(f"La operacion no existe, {option}!!")
                                                    
                print(f"The result is: {result} \n")
                
                respuesta_teclado = input("Deseas continuar, presiona y \n")
                if respuesta_teclado != 'y' or respuesta_teclado.upper() != 'Y':
                    break
                                                    
            else:
                print("Error: selec a valid option")
                
        except ValueError as er:
            print(f"Los valores ingresados no son validos: {er}, ingrese un valor entero")
        except Exception as er:
            print(f"Datos Incorrectos: {er}")

calculator()