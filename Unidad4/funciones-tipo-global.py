
nombre = "Nicolas"  # Variable Global o Externa

def saludo():    
    global nombre       #  Ya no es una variable totalmente local a funcion
    print(f"Hola, {nombre}")
    
#nombre = "Agustin"  # Variable Global o Externa
saludo()
