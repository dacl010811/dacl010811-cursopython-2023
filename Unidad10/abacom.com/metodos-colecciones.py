



# Metodos disponibles en el tipo de dato STRING

cadena = "hola Mundo en Python"
cadena_1 = 'hola Mundo, JAVA'

cadena_mesaje = "hola mundo, en \"python\"" #  "Hola mundo, en 'python'"
cadena_mesaje = 'hola mundo, en "python"' #  "Hola mundo, en 'python'"

print(cadena)
print(cadena_1)
print(cadena_mesaje)

# Utilizando  métodos de la clase  String upper()----> Mayusculas
print(f"Upper de una cadena :{cadena.upper()}")
print(f"Upper de una cadena :{cadena_1.upper()}")
print(f"Upper de una cadena :{cadena_mesaje.upper()}")

# Utilizando  métodos de la clase  String lower()----> minisculas

print("------------- Minusculas-------------------")

print(f"Lower de una cadena : {cadena.lower()}")
print(f"Lower de una cadena : {cadena_1.lower()}")
print(f"Lower de una cadena : {cadena_mesaje.lower()}")

print("------------- Capitalizar-------------------")

print(f"Capitalizar de una cadena : {cadena.capitalize()}")
print(f"Capitalizar de una cadena : {cadena_1.capitalize()}")
print(f"Capitalizar de una cadena : {cadena_mesaje.capitalize()}")


print("------------- Title-------------------")

cadena = "vacaciones en paris"
cadena_1 = "felices navidades"
cadena_mesaje = "felices vacaciones"

print(f"Title de una cadena : {cadena.title()}")
print(f"Title de una cadena : {cadena_1.title()}")
print(f"Title de una cadena : {cadena_mesaje.title()}")

print("------------- Count()-------------------")

cadena = "vacaciones en paris, tambien en Quito y en Cuenca"
cadena_1 = "felices navidades, navidades loja, navidades Cuenca"
cadena_mesaje = "felices vacaciones, felcidades felicidades a todos"

print(f"Count de una cadena : {cadena.count('en')}")
print(f"Count de una cadena : {cadena_1.count('navidades')}")
print(f"Count de una cadena : {cadena_mesaje.count('felicidades')}")


print("------------- Find()-------------------")

cadena = "vacaciones en paris, tambien en Quito y en Cuenca"
        #[01        1112                                        ]
cadena_1 = "felices navidades, navidades loja, navidades Cuenca"
cadena_mesaje = "felices vacaciones, felcidades felicidades a todos"

print(f"Find de una cadena : {cadena.find('en')}")
print(f"Find de una cadena : {cadena_1.find('xnavidades')}")
print(f"Find de una cadena : {cadena_mesaje.find('felicidades')}")


print("------------- rFind()-------------------")

cadena = "vacaciones en paris, tambien en Quito y en Cuenca"
        #[01        1112                          45              ]
cadena_1 = "felices navidades, navidades loja, navidades Cuenca"
cadena_mesaje = "felicidades vacaciones, felcidades felicidades a todos"
                #0                                  45 
print(f"rFind de una cadena : {cadena.rfind('en')}")
print(f"rFind de una cadena : {cadena_1.rfind('xnavidades')}")
print(f"rFind de una cadena : {cadena_mesaje.rfind('felicidades')}")
print(f"rFind de una cadena : {cadena_mesaje.find('felicidades')}")

print("------------- isDigit()-------------------")

cadena_mesaje = "200"
print(f"isDigit de una cadena : {cadena_mesaje.isdigit()}")

print("------------- isalnum()-------------------")
variable_cadena = "ABC_10034po@"
print(f"isalnum de una cadena : {variable_cadena.isalnum()}")


print("------------- istitle()-------------------")
variable_cadena = "Hola Mundo Python"
print(f"istitle de una cadena : {variable_cadena.istitle()}")


print("------------- startwith()-------------------")
variable_cadena = "Hola Mundo Python"
print(f"startwith de una cadena : {variable_cadena.startswith('Hola')}")


print("------------- split()-------------------")
cadena_1 = "felices navi-dades, navidades loja, navidades Cuen-ca"
lista_palabras = cadena_1.split(',')[2]
print(f"split de una cadena : {lista_palabras}")


print("------------- join()-------------------")
cadena_1 = "Felices navidades desde Quito"
cadena_aux  = "+".join(cadena_1)

print(f"join de una cadena 1 : {cadena_aux}")


print("------------- strip()-------------------")
cadena_1 = "         Felices navidades desde Quito               "
print(f"strip de una cadena 1 : {cadena_1.strip()}")



print("------------- replace()-------------------")
cadena_1 = "Felices navidades desde Quito"
print(f"replace de una cadena 1 : {cadena_1.replace('e','E')}")



print("------------- isspace()-------------------")
cadena_1 = "            "
print(f"isspace de una cadena 1 : {cadena_1.isspace()}")