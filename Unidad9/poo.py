

class Persona():
    """Representa un objeto de la vida: persona"""
    
    #Atributos de Clase
    contador_personas = 0
    etnia_personas = "Afro"
    
    #Constructor
    def __init__(self,nombre=None,apellido=None,edad=None):
                
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    @classmethod
    def dormir(cls):
        print("Estoy durmiendo!!  - Metodo de Clase ")
    
    def trabajar(self):
        print("Estoy trabajando!!")
    
    @classmethod
    def correr(cls):
        print("Estoy corriendo!! - Metodo de Clase")
    
    def respirar(self):
        print("Estoy vivo!!")


#Acceder a los atributos y metodos de clase  
#Atributos
Persona.contador_personas = 10     #  set()
Persona.etnia_personas = "Meztiso"     #  set()
    
# Crear instancias de una clase    
persona_1  = Persona("Darwin","Calle", 40)    
#Acceder a los atributos de instancia
print(persona_1.nombre)
print(persona_1.apellido)
print(persona_1.edad)


# Acceder a los metodos de clase
Persona.dormir()
Persona.correr()


#Acceder a los metodos de instancia
persona_2 = Persona("Maria","Calle",4)

persona_2.respirar()
persona_2.trabajar()

