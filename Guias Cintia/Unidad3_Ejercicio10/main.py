'''10) En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también 
al final del día calcular la cantidad de dinero que se ha depositado. Se deberán crear dos clases, la clase cliente 
y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, 
extraer, mostrar_total. La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, 
operar y deposito_total.'''
from class_clientes import Clientes
from class_banco import Banco

def __main__():
   
    banco1 = Banco()
    banco1.operar()
    banco1.deposito_total()

if __name__=='__main__':
    __main__()




