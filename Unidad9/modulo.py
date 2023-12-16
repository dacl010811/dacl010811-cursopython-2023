


class Persona():
    contador_personas = 0
    
    def __init__(self,cedula,nombre,apellido=None,celular=None,direccion=None):
        if len(cedula) > 10 and len(nombre) > 4:            
            try:
                self.cedula = cedula
                self.nombre = nombre
            except Exception as er:
                print("")
        else:
            print("Datos Invalidos!!")
        
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
        

# Diseñar algo relacionado a un Zoologico

class Animal():
    
    def __init__(self, nombre,especie,edad,region) -> None:
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.region = region
    
    def __str__(self) -> str:
        return "A:[ {0}, {1}, {2}, {3} ]".format(self.nombre, self.especie,self.edad,self.region)
           
    def comer(self):
        print("Estoy comiendo: Clase Aminal")
        
    def dormir(self):
        print("Estoy durmiendo: Clase Aminal")

class Mamifero(Animal):
    
    def __init__(self, nombre,especie,edad,region,pelaje,color):
        super().__init__( nombre,especie,edad,region)
        self.pelaje = pelaje
        self.color = color
    
    def __str__(self) -> str:
        return "[Soy un Mamifero: {0} {1}]".format(self.pelaje,self.color)
    
    def amamantar(self):
        print("Estoy amamantando a las crias")
        
    def comer(self):
        print("Estoy comiendo, pero soy un mamifero")
    
    def dormir(self):
         print("Estoy durmiendo como un mamifero")


class Ave(Animal):
    
    def __init__(self, nombre,especie,edad,region,color):
        super().__init__( nombre,especie,edad,region)        
        self.color = color
     
    def __str__(self) -> str:
        return "[Soy un Ave: {0}]".format(self.color) 
        
    def volar(self):
        print ("Estoy volando, soy una Ave")


class Reptil(Animal):
    
    def __init__(self, nombre,especie,edad,region,tipo_piel):
        super().__init__( nombre,especie,edad,region)        
        self.tipo_piel = tipo_piel
        
    def __str__(self) -> str:       
        return "[Soy un reptil: {0} {1}]".format(super().__str__(),self.tipo_piel)
    
    def arrastrarse(self):
        print("Estoy arrastrandome")


class Anfibio(Animal):
    
    def __init__(self, nombre,especie,edad,region,tipo_anfibio):
        super().__init__( nombre,especie,edad,region)        
        self.tipo_anfibio = tipo_anfibio
        
    def __str__(self) -> str:
        return "[Soy un Anfibio: {0} {1} ]".format(super().__str__(),self.tipo_anfibio)


class AreaZoologico():
    
    def __init__(self,nombre,capacidad):
        self.nombre = nombre
        self.capacidad = capacidad        
        self.aminales = []
        
    def agregar_animal(self, animal):
        if len(self.aminales) < self.capacidad:
            self.aminales.append(animal)
            print(f" El animal: {animal} ha sido agregado al area : {self.nombre}")
        else:
            print(f" No hay espacio disponible para agregarlo")
    
    
class Zoologico():
    
    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.areas = []
        
    def agregar_area(self, area):
        self.areas.append(area)
        print(f"El creado el area : {area.nombre}, en el zoologico!!")
        

# Crear objetos o instancias de una clase

leon = Mamifero("Simba","Leon",5,"Africa","Suave","Cafe")
perro = Mamifero("Dog","Perro",5,"Suiza","Suave","Negro")

print("-----------------------------------------------")

aguila = Ave("Aguila Real","Aguila",3,"Sierra","Cafe")
condor = Ave("Condor Sierra","Condor",10,"Sierra","Negro")

print("-----------------------------------------------")

serpiente = Reptil("Boa","Serpiente",10,"Amazonia","escamas")

print("-----------------------------------------------")

#Areas del Zoologico
zona_maniferos = AreaZoologico("Aminales Mamiferos",5)
zona_maniferos.agregar_animal(leon)
zona_maniferos.agregar_animal(perro)

zona_aves = AreaZoologico("Aminales Aves",10)
zona_aves.agregar_animal(aguila)
zona_aves.agregar_animal(condor)

zona_reptiles = AreaZoologico("Aminales Reptiles",8)
zona_reptiles.agregar_animal(serpiente)


zoologico_aventura = Zoologico("Aventura Animal","Quito Norte")
zoologico_aventura.agregar_area(zona_maniferos)
zoologico_aventura.agregar_area(zona_aves)
zoologico_aventura.agregar_area(zona_reptiles)


# Parametros por defecto en el Constructor de Clase

persona_1 = Persona("1102587418","Darwin","Apellido","0565656565","direccion")
print(persona_1)

persona_2 = Persona("1252588524","Abcde")
print(persona_2)

