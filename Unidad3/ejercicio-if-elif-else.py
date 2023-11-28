

# Ingresar NOTAS
# Sobresaliente = 10
# Notable :  Nota >= 8 hasta <= 9
# Buena  :  Nota == 7
# Regular :  NOta  5 y 6  
# Insuficiente  < 5

nota_materia = float(input('Ingresa la nota de la materia: \n'))

if nota_materia == 10:
    print('La nota es sobresaliente!!, Felicitaciones')
elif nota_materia >= 8 and nota_materia <=9:
    print('Tu nota es Notable!!, excelente')
elif nota_materia >= 7 and nota_materia <= 7.9:
    print('Tu nota es Buena!!, sigue estudiando')
elif nota_materia == 5 or nota_materia == 6:
    print('Tu nota es Regular!!')
elif  nota_materia > 1  and nota_materia < 5: #  2,3  y 4
    print('Tu nota es Insuficiente!!')
elif nota_materia == 1 or nota_materia == 0 :
    print('Perdiste el semestre!!')
else:
    print ('La nota que ingresaste sobrepasa el formato de 10/10')
    
    

