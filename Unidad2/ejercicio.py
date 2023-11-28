cantidad_a_pagar = 0.0
for contador in range(1,3):
    datos_entrada = input(f'Ingrese los datos producto {contador} : \n')
    
    codigo_producto = int(datos_entrada.split(' ')[0])
    unidades_producto = int(datos_entrada.split(' ')[1])
    precio_producto = float(datos_entrada.split(' ')[2])
    
    cantidad_a_pagar += (float(unidades_producto) * float(precio_producto))

print(f"VALOR A PAGAR : R$ {cantidad_a_pagar:.2f}")