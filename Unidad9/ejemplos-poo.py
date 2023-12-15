



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
        

#Crear objetos o instancias de la clase Persona

persona_1 = Persona("1104857588","Darwin","Loja1","0998855244","Avenida 10 de Agosto y Sucre")
persona_2 = Persona("1104857581","Jose","Loja2","0998855255","Avenida 10 de Agosto y Sucre")
persona_3 = Persona("1104857583","Alexis","Loja3","0998855266","Avenida 10 de Agosto y Sucre")
persona_4 = Persona("1104857584","Rodrigo","Loja4","0998855277","Avenida 10 de Agosto y Sucre")
persona_5 = Persona("1104857585","Cesar","Loja5","0998855288","Avenida 10 de Agosto y Sucre")
persona_6 = Persona("1104857586","Ximena","Loja6","0998855278","Avenida 10 de Agosto y Sucre")
persona_7 = Persona("1104857587","Nicolas","Loja7","0998855278","Avenida 10 de Agosto y Sucre")


print(f" Persona 1 :  {persona_1}")
print(f" Persona 2 :  {persona_2}")
print(f" Persona 3 :  {persona_3}")
print(f" Persona 4 :  {persona_4}")
print(f" Persona 5 :  {persona_5}")
print(f" Persona 6 :  {persona_6}")
print(f" Persona 7 :  {persona_7}")


