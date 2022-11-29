#ACTIVIDAD PRÁCTICA UNIDAD 3

'''1)Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” 
y “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos por consola.'''

'''NO FUNCIONA. Creo que no es exactamente lo que piden pero no entiendo qué tenemos que hacer. '''
# class Persona:

#     @property             #Getter
#     def nombre(self):
#         return self.__nombre

#     @property             #Getter
#     def edad(self):
#         return self.__edad
    
#     @nombre.setter        #Setter
#     def nombre(self, nombre):
#         self.__nombre=nombre 
    
#     @edad.setter        #Setter
#     def edad(self, edad):
#         self.__edad=edad 
    
#     def __str__(self):
#         return f'{self.__nombre} tiene {self.__edad} años.'


# #PROGRAMA PRINCIPAL

# persona1=Persona()
# persona2=Persona()
# print(persona1)
# print(persona2)

'''2) Agregarle a la clase anterior un constructor que reciba nombre y edad.
3) Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.'''
'''no termino de entedner la función del los guiones para hacer privados los atributos ya que si los consulto, los puedo ver'''
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
#         return self.__edad >= 18  #retorna true si se cumple la condición

# #PROGRAMA PRINCIPAL

# persona1 = Persona("Cintia", 39)
# print(persona1)
# print(persona1.es_mayor_de_edad())

'''¿Por qué puedo modificar y consultoar los artibutos como siguen si los puse probados? ESTUDIAR!!!!'''
# persona1.edad = 38
# print(persona1.nombre)

'''4) Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la del objeto actual.'''
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
#         return self.__edad >= 18   #retorna true si se cumple la condición

# #Ejercicio 4
#     def es_mayor_que(self, persona):
#         if self.__edad > persona.__edad:
#             rta = f'{self.__nombre} es mayor que {persona.__nombre}'
#         elif self.__edad < persona.__edad:
#             rta = f'{self.__nombre} es menor que {persona.__nombre}'
#         else:
#             rta = "Ambas personas tienen la misma edad"
#         return rta

# #PROGRAMA PRINCIPAL

# persona1 = Persona("Cintia", 39)
# persona2 = Persona("Juanjo", 43)
# print(persona1)
# print(persona2)
# print(persona1.es_mayor_que(persona2))

'''5) Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad mayor.'''
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
#         return self.__edad >= 18   #retorna true si se cumple la condición

# #Ejercicio 4
#     def es_mayor_que(self, persona):
#         if self.__edad > persona.__edad:
#             rta = f'{self.__nombre} es mayor que {persona.__nombre}'
#         elif self.__edad < persona.__edad:
#             rta = f'{self.__nombre} es menor que {persona.__nombre}'
#         else:
#             rta = "Ambas personas tienen la misma edad"
#         return rta

# #Ejercicio 5
#     def get_mayor(self, persona):
#         if self.__edad > persona.__edad:
#             rta = f'La edad de la persona mayor de las dos comparadas, es {self.__edad} años'
#         elif self.__edad < persona.__edad:
#             rta = f'La edad de la persona mayor de las dos comparadas, es {persona.__edad} años'
#         else:
#             rta = f'Ambas personas tienen la misma edad, {self.__edad} años'
#         return rta


# #PROGRAMA PRINCIPAL

# persona1 = Persona("Cintia", 39)
# persona2 = Persona("Juanjo", 43)
# print(persona1)
# print(persona2)
# print(persona1.es_mayor_que(persona2))
# print(persona1.get_mayor(persona2))

'''6) Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota 
del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado 
de la nota y si ha aprobado o no.'''
# class Alumno:
#     def __init__(self, nombre, nota):
#         self.nombre = nombre
#         self.nota = nota 
    
#     def __str__(self):
#         if self.nota >= 6:
#             rta = f'{self.nombre} tiene una nota de {self.nota} y está aprobado'
#         else:
#             rta = f'{self.nombre} tiene una nota de {self.nota} y no está aprobado'
#         return rta

# #PROGRAMA PRINCIPAL  

# alumno1 = Alumno('Juan', 8)
# print(alumno1.nombre)
# print(alumno1.nota)
# print(alumno1)
# # alumno1.nota = 9
# # print(alumno1.nota)
# # print(alumno1)

'''7) Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para 
inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es 
(equilátero, isósceles o escaleno).'''
# class Triangulo:
#     def __init__(self, lado1, lado2, lado3):
#         self.lado1 = lado1
#         self.lado2 = lado2
#         self.lado3 = lado3
    
#     def lado_mayor(self):
#         if lado1 > lado2 >= lado3:
#             rta = self.lado1
#         elif lado1 > lado3 >= lado2:
#             rta = self.lado1
#         elif lado2 > lado1 >= lado3:
#             rta = self.lado2
#         elif lado2 > lado3 >= lado1:
#             rta = self.lado2
#         elif lado3 > lado1 >= lado2:
#             rta = self.lado3
#         elif lado3 > lado2 >= lado3:
#             rta = self.lado3
#         elif lado1 == lado2 == lado3:
#             rta = self.lado1
#         return f'el mayor de los lados mide {rta}'
    
#     def tipo_de_triangulo(self):
#         if lado1 != lado2 != lado3:
#             rta = 'Es un triángulo escaleno'
#         elif lado1 == lado2 == lado3:
#             rta = 'Es un triángulo equilátero'
#         else:
#             rta = 'Es un triángulo isósceles'
#         return rta

#     def __str__(self):
#         return f'{self.tipo_de_triangulo()} y {self.lado_mayor()}'

# #PROGRAMA PRINCIPAL

# lado1 = int(input('Ingrese la medida de uno de los lados del triángulo:'))
# lado2 = int(input('Ingrese la medida de otro de los lados del triángulo:'))
# lado3 = int(input('Ingrese la medida del último de los lados del triángulo:'))

# triangulo1 = Triangulo(lado1, lado2, lado3)
# print(triangulo1)

'''8)Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el 
método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una 
e imprimir los resultados obtenidos. Llamar a la clase Calculadora.'''
# class Calculadora:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def suma(self):
#         suma = self.num1 + self.num2
#         return suma

#     def resta(self):
#         resta = self.num1 - self.num2
#         return resta

#     def multiplicacion(self):
#         mult = self.num1 * self.num2
#         return mult

#     def division(self):
#         div = self.num1 // self.num2
#         return div
    
#     def __str__(self):
#         return f'Suma: {self.suma()}; \nResta: {self.resta()}; \nMultiplicación: {self.multiplicacion()}; \nDivisión: {self.division()}'

# # PROGRAMA PRINCIPAL

# num1 = int(input('Ingrese un número entero:'))
# num2 = int(input('Ingrese otro número entero:'))

# print(Calculadora(num1, num2))

'''SEGUIR'''
'''9) Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono 
y el email. Además deberá mostrar un menú con las siguientes opciones: Añadir contacto, Listar contactos, Buscar 
contacto, Editar contacto, Cerrar agenda.'''
class Agenda:

    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

#No entiendo por qué no funciona este while...debería acabar el ciclo cuando el nombre es vacio pero no lo hace
    
    def anadir_contacto(self):   
        lista_contactos = []
        nom = input ('Ingrese el Nombre: ')
        while nom != ' ':
            tel = input ('Ingrese el Teléfono: ')
            email = input ('Ingrese el E-mail: ')
            contacto = Agenda(nom, tel, email)
            lista_contactos.append(contacto)
            nom = input ('Ingrese el Nombre: ')
            return lista_contactos 
    
    def listar_contactos(self, lista_contactos):
        for contacto in lista_contactos:
            print(contacto)
        
    def buscar_contacto(self, lista_contactos):
        for contacto in lista_contactos:
            if contacto == lista_contactos.nom:
                print('lista_contacto.tel', 'lista_contacto.email')

    def editar_contacto(self):
        pass

    def cerrar_agenda(self):
        pass

# PROGRAMA PRINCIPAL

contacto1 = Agenda('Cintia', 3562408801, 'cintiagoddio@gmail.com')
Agenda.anadir_contacto(contacto2)

'''10) En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también 
al final del día calcular la cantidad de dinero que se ha depositado. Se deberán crear dos clases, la clase cliente 
y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, 
extraer, mostrar_total. La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, 
operar y deposito_total.'''
# class Clientes:

#     def __init__(self, nombre, cantidad):
#         self.nombre = nombre


 