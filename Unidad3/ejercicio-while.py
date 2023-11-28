




# Ejercicio de las tablas de multiplicar
#  9 X 1
#  9 X 2

contador = 0

tabla =  int(input('Ingresa el # de la tabla que deseas generar: \n'))
limite = int(input('Ingresa el lìmite de la tabla a generar: \n'))

while contador <= limite:    
    contador +=1
    
    if ( contador % 2 != 0 ) : # Numero PAR
        print(f" {tabla} * {contador} = { tabla * contador}")        
        continue # break    
        
else:
    print("Siempre entrare cuando todo vaya bien!!")
        
print("Se termino el while")

