class Persona():
    contador_personas = 0
    
    def __init__(self,cedula,nombre, apellido,celular,direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.direccion = direccion
    
    def __str__(self) -> str:        
        return "Persona [ {} - {} - {} ]".format(self.cedula,self.nombre,self.apellido)
    
    def saludar(self):
        print("Hola, buenos dias")
        
    def dormir(self):
        print("Buenas noches")
    
    def trabajar(self):
        print("Estoy trabajando")