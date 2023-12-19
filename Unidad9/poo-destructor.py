


class Pelicula():
    
    def __init__(self,nombre,duracion, lanzamiento) -> None:
        self.nombre = nombre
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        
        print("Estoy en el constructor de la clase pelicula en python")
        
    
    def __str__(self):
        return f"self.nombre :{self.nombre},self.duracion :{self.duracion},self.lanzamiento :{self.lanzamiento}"
    
    
    def __del__(self):
        print("Estoy eleiminando un objeto!!")
        
    def __len__(self) -> int:
        return self.duracion
        
        

class Catalogo:
    
    #peliculas = []  # Esta lista contendrá objetos de la clase Pelicula
    
    def __init__(self,peliculas=[]):
        self.peliculas = peliculas
        
    def agregar(self,p):  # p será un objeto Pelicula
        self.peliculas.append(p)
        
    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)
            
    def __str__(self) -> str:
        catalogo_accion = ""
        for p in self.peliculas:
            catalogo_accion += p.nombre + " - "
        return catalogo_accion

#catalogo_accion = Catalogo([Pelicula("La Momia 1",120,"2000"),Pelicula("La Momia 2",160,"2005")])
#catalogo_accion.agregar(Pelicula("Thor 1",180,"2008"))
#catalogo_accion.agregar(Pelicula("El hombre Aranna ",220,"2006"))

#print(catalogo_accion)


class Automovil():
    
    __kilometraje = 0
    
    def __init__(self,marca,tipo,color,precio=None,pais=None) -> None:
        self.marca = marca
        self.tipo = tipo
        self.color = color
        self.precio = precio
        self.pais = pais
    
    def  __reset_kilometraje_fabrica(self):
        __kilometraje = 0
        
    # IMplementacion de un metodo get() y set()--  JAVA
    def retorno_kilometraje(self):
        return self.__kilometraje
    
    def fijar_kilometraje(self,kilometraje):
        self.__kilometraje = kilometraje
    
      
    
automovil_1 = Automovil("Chevrolet", "SUV","Negro")
automovil_1.fijar_kilometraje(200)
print(f"K: {automovil_1.retorno_kilometraje()}")


automovil_2 = Automovil("KIA", "SOLTS","Gris")
print(f"K: {automovil_2.retorno_kilometraje()}")
    
    



