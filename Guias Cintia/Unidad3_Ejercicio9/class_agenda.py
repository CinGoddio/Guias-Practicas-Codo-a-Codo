from class_contacto import Contacto

class Agenda:
    #lista_contactos = []

    def __init__(self): #lista_contactos = []):
        #Agenda.lista_contactos = lista_contactos
        self.lista_contactos = []
        cerrada = False
 
    def anadir_contacto(self, nombre, telefono, email): 
        contac = Contacto(nombre, telefono, email)  # esto me permite no crear el contacto aparte en el programa principla, sino crearlo cuando intento usar el método añadir contacto
        #Agenda.lista_contactos.apend(contac)   
        self.lista_contactos.append(contac)
        print('Contacto añadido')
   
    def listar_contactos(self):
        for contac in self.lista_contactos: #Agenda.lista_contactos:
            print(contac)
        
    def buscar_contacto(self, nombre): #Usar un find
        for contac in self.lista_contactos:
            if contac.nombre == nombre: 
                print(contac) 

    def editar_contacto(self):
        pass
    
    def cerrar_agenda(self):
        self.cerrada = True
        return print(f'La agenda fue cerrada.')
        