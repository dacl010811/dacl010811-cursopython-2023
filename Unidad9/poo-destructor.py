


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

catalogo_accion = Catalogo([Pelicula("La Momia 1",120,"2000"),Pelicula("La Momia 2",160,"2005")])
catalogo_accion.agregar(Pelicula("Thor 1",180,"2008"))
catalogo_accion.agregar(Pelicula("El hombre Aranna ",220,"2006"))

print(catalogo_accion)


