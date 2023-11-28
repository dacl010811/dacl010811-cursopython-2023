


#Reglas:
# Las expresiones en Python se evaluan de izquierda a derecha
# Las prioridades de las expresiones se determinan por por un orden dentro de la expresion


x = int(input("Ingresar un valor entero 1")) #  1
y = int(input("Ingresar un valor entero 2")) #  2
z = int(input("Ingresar un valor entero 3")) #  3

resultado =  (( x +y +z) * 10 + (x**2) / (y//2)+ 10 -5 + (z % 2)) != 0  and  ((2+4/2) == -1)
            # (( 1 +2 +3) * 10 + (1**2) / (2//2)+ 10 -5 + (3 % 2)) != 0  and  ((2+4/2) == -1)
            # ((6) * 10 + (1) / (1) + 10 -5 + (1)) != 0  and  ((2+4/2) == -1)
            # ((6) * 10 + (1) / (1) + 10 -5 + (1)) != 0  and  (4 == -1)
            # (60 + 1 + 10 -5 + 1) != 0  and  (4 == -1)
            # (60 + 1 + 10 -5 + 1) != 0  and  (4 == -1)
            #     67 != 0 and  False
            #       True and  False
            #        False                        
            
            #En pyton existe 2 tipos de Division :
            # Division Entrera, se la representa con el simbolo "//"      3 // 2 = 1.5    --> 1 Parte Entera
            #                                                             10 // 3 = 3.33  --> 3 Parte Entera
            # Division NOrmal  :    10 / 4 = 2.5

print("El resultado de la expresion es = " + str(resultado))



