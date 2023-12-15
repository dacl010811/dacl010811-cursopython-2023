

class Persona():
    contador_personas = 0
    
    def __init__(self,cedula,nombre, apellido,celular,direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.direccion = direccion
    
    def __str__(self) -> str:
        return "Persona [ {0} - {1} - {2} ]".format(self.cedula,self.nombre,self.apellido)
    
    def saludar(self):
        print("Hola, buenos dias")
        
    def dormir(self):
        print("Buenas noches")
    
    def trabajar(self):
        print("Estoy trabajando")
        
# La herencia :  Concepto vinculado a la POO que permite reducir, reutilizar cierto  comportamieno
#                de las clases

class Cliente(Persona):
        
    def __init__(self,cedula,nombre, apellido,celular,direccion,direccion_trabajo,telefono_casa):
        super().__init__(cedula,nombre, apellido,celular,direccion)
        self.direccion_trabajo = direccion_trabajo
        self.telefono_casa = telefono_casa
     
    def __str__(self) -> str:
        return "Cliente [ {0} - {1} - {2} ]".format(self.cedula,self.nombre,self.apellido)
                   
    def comprar(self):
        print("Voy a comprar")
        

# Crear instancias de cliente
cliente_1  = Cliente("19055454545","Nicolas","Quito","0998877544","Quito y Amazonas","Amazonas","022548754")
print(cliente_1)

cliente_1.dormir()
cliente_1.trabajar()
cliente_1.comprar()
        
        