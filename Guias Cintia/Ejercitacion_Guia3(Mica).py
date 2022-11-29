#1) Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos por consola.
#2) Agregarle a la clase anterior un constructor que reciba nombre y edad.

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property    
    def edad(self):
        return self.__edad
    
    @nombre.setter
    def nombre (self, nombre):
        self.__nombre= nombre
        
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    
    def __str__(self):
        return f'La persona se llama: {self.__nombre} y tiene {self.__edad} años'

p1 = Persona("Federico", 41)
print(p1)

p1.edad = 45
p1.nombre= "Catalina"
print(p1)

#3) Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.

