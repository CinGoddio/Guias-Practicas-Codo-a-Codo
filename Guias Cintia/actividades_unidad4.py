#ACTIVIDAD PRÁCTICA UNIDAD 4

'''1) Crea la clase Vehiculo, extiende la clase y realiza la siguiente implementación:...'''
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        self.vehiculos = []
    
    def agregar_vehiculos(self, vehic):
        self.vehiculos.append(vehic)
        

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def agregar_vehiculos(self, vehic):
        super().append(vehic)

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        Vehiculo.__init__(self, color, ruedas)
        self.carga = carga

    def agregar_vehiculos(self, vehic):
        super().append(vehic)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def agregar_vehiculos(self, vehic):
        super().append(vehic)

class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def agregar_vehiculos(self, vehic):
        super().append(vehic)

#PROGRAMA PRINCIPAL
coche1 = Coche('Rojo',4, '120 k/h', '800 cc')
camioneta1 = Camioneta('Azul', 4, '10000 kg')
bicicleta1 = Bicicleta('Verde', 2, 'Urbana')
motocicleta1 = Motocicleta('Blanca', 2, '50 k/h', '100 cc')

print(coche1)
'''NO FUNCIONA LA FUNCIÓN agregar_vehiculos'''
#Coche.agregar_vehiculos(coche1)
# Vehiculo.agregar_vehiculos(camioneta1)
# Vehiculo.agregar_vehiculos(bicicleta1)
# Vehiculo.agregar_vehiculos(Vmotocicleta1)

'''2) Continua con el ejercicio anterior y realiza una función llamada catalogar() que reciba la lista de 
vehiculos y los recorra mostrando el nombre de su clase y sus atributos.'''


        