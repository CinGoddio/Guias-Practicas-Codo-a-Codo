class Clientes:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0
    
    def depositar(self, importe):
        estado = False
        if importe > 0:
            self.cantidad += importe
            estado = True
        return estado
        
    def extraer(self, importe):
        estado = False
        if importe <= self.cantidad:
            self.cantidad -= importe
            estado = True
        return estado

    def mostrar_total(self):
        return self.cantidad

    def __str__(self):
        return f'{self.nombre} tiene depositado {self.cantidad}'