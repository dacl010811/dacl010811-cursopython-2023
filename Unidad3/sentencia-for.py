

# Sentencia for en su estructura basica tenemos 2 palabras reservadas a utilizar
# for  y la  in

cadena = "1234567890"
        # [0] 123456789 ---- >   [0] --> Indice me devuelve el caracter 1
        # [1] 123456789 ---- >   [1] --> Indice me devuelve el caracter 2
        # [2] 123456789 ---- >   [2] --> Indice me devuelve el caracter 3
        # [3] 123456789 ---- >   [3] --> Indice me devuelve el caracter 4
        # [4] 123456789 ---- >   [4] --> Indice me devuelve el caracter 5
        # [5] 123456789 ---- >   [5] --> Indice me devuelve el caracter 6
        # [6] 123456789 ---- >   [6] --> Indice me devuelve el caracter 7

for i in cadena:
    print(i)
    
# listas en python :    "[]" 

lista_elementos = ["Darwin" ,1,  2, 3, 4, 5, 6, 7, 8, 9, "10", "11", "12", "13", True, False, 10.0, 5.2, [1.2] ]
                #    [0]   [1]  [1] .......................................................    

contador = 0
for elemento in lista_elementos:
    print(f" Elemento [{contador}] : {elemento}")
    contador +=1
    
