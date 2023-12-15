


class Banco():
    codigo = 0
    direccion = None
    
    def __init__(self,nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
    
    @classmethod
    def administracion(cls):
        print("Estoy en la administarcion del banco - MC")
        
    def mantenimiento(self):
        print("Mantenimiento - MI")
        

class Cuenta_Bancaria():
    pass

class Cliente():
    pass

class ATM():
    pass

class TransaccionesAtm():
    pass

class Cuenta_Corriente():
    pass

class Cuenta_Ahorro():
    pass

#Atributos de clase y metodos de clase
Banco.codigo = "Codigo"
Banco.direccion = "Direccion 1"
Banco.administracion()

#Atributos de Instancia y metodos de instancia

banco_1 = Banco("Pichincha","Amazonas")
print(f"B1 = {banco_1.nombre}")
print(f"B1 = {banco_1.direccion}")

banco_1.mantenimiento()

