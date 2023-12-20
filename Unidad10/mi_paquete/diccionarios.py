
#  Se definen con {} deben generarse los datos en formato   "clave:valor"  o "key:value" separador por ,
colores = { "amarillo":"yellow", "azul":"blue", "verde":"green", '0' : 452 }

print(f" {colores['amarillo']}")
print(f" {colores['azul']}")
print(f" {colores['0']}")              #  colores[0] = nuevo_valor  # colores[1,2,2,8] =
                                                                        #   0
                                                                        
# Metodos avanzados

print("Metodo GET")
print (f"{colores.get('azul')}" )
print (f"{colores.get('amarillo')}" )    
print (f"{colores.get('verde')}" )        
print (f"{colores.get('0')}" )   
  
print (f"{colores.get(0,'No lo encontre')}" )    
                                                   
print("Metodo keys")    
llaves = colores.keys()
print(type(llaves))
print(llaves)

print("Metodo values")    
valores = colores.values()
print(type(valores))
print(valores)
                               
# Metodo items()

print(" Metodo items()") 
diccionario_items =  colores.items() # dict_items( [ ('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green'), ('0', 452) ])
print(diccionario_items)  

for clave,dato in colores.items():
    print(f"{clave}:{dato}")

colores.pop('amarillo')
colores.pop('verde')
colores.pop('0')
colores.pop('000000','N0 existe!!')

print(colores)
colores.clear()
print(colores)