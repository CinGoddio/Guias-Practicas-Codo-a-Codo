from class_clientes import Clientes

class Banco:

    def __init__(self):
        self.cliente1 = Clientes('Juan')
        self.cliente2 = Clientes('Pedro')
        self.cliente3 = Clientes ('Ana')

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(250)
        self.cliente3.depositar(500)
        self.cliente3.extraer(100)

    def deposito_total(self):
        total = self.cliente1.mostrar_total() + self.cliente2.mostrar_total() + self.cliente3.mostrar_total()
        print(f'La suma total de depósitos del banco es de {total}')
        print(self.cliente1)
        print(self.cliente2)
        print(self.cliente3)
        