#ACTIVIDAD PRÁCTICA UNIDAD 3

'''1)Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” 
y “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos por consola.'''
# class Persona:

#     @property             #Getter
#     def nombre(self):
#         return self.nombre

#     @property             #Getter
#     def edad(self):
#         return self.edad
    
#     @nombre.setter        #Setter
#     def nombre(self, nombre):
#         self.nombre=nombre 
    
#     @edad.setter        #Setter
#     def edad(self, edad):
#         self.edad=edad 
    
#     def __str__(self):
#         return f'{self.nombre} tiene {self.edad} años.'


# #PROGRAMA PRINCIPAL

# persona1=Persona()
# persona2=Persona()
# print(persona1)
# print(persona2)

'''2) Agregarle a la clase anterior un constructor que reciba nombre y edad.
3) Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.'''

# class Persona:

# #Ejercicio 2
#     def __init__(self, nombre, edad):
#         self.__nombre = nombre
#         self.__edad = edad        

#     @property             #Getter
#     def nombre(self):
#         return self.__nombre

#     @property             #Getter
#     def edad(self):
#         return self.__edad
    
#     @nombre.setter        #Setter
#     def nombre(self, nombre):
#         self.__nombre = nombre 
    
#     @edad.setter        #Setter
#     def edad(self, edad):
#         self.__edad = edad 
    
#     def __str__(self):
#         return f'{self.__nombre} tiene {self.__edad} años.'
    
# #Ejercicio 3
#     def es_mayor_de_edad(self):
#         return self.__edad >= 18


# #PROGRAMA PRINCIPAL

# persona1 = Persona("Cintia", 39)
# print(persona1)
# print(persona1.es_mayor_de_edad())

'''4) Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la del objeto actual.'''

class Persona:

#Ejercicio 2
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad        

    @property             #Getter
    def nombre(self):
        return self.__nombre

    @property             #Getter
    def edad(self):
        return self.__edad
    
    @nombre.setter        #Setter
    def nombre(self, nombre):
        self.__nombre = nombre 
    
    @edad.setter        #Setter
    def edad(self, edad):
        self.__edad = edad 
    
    def __str__(self):
        return f'{self.__nombre} tiene {self.__edad} años.'
    
#Ejercicio 3
    def es_mayor_de_edad(self):
        return self.__edad >= 18

#Ejercicio 4
    def es_mayor_que(self, persona):
        return self.__edad >= 18

#PROGRAMA PRINCIPAL

persona1 = Persona("Cintia", 39)
print(persona1)
print(persona1.es_mayor_de_edad())