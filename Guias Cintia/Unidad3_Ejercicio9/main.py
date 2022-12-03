'''9) Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono 
y el email. Además deberá mostrar un menú con las siguientes opciones: Añadir contacto, Listar contactos, Buscar 
contacto, Editar contacto, Cerrar agenda.'''

from class_contacto import Contacto
from class_agenda import Agenda

# PROGRAMA PRINCIPAL

def __main__():

    agenda1 = Agenda()
    #print(agenda1)       # imprime los datos de memoria del objeto
    agenda1.anadir_contacto('Cintia', 3562408801, 'cintiagoddio@gmail.com') #imprime "Contacto añadido"
    agenda1.anadir_contacto('Juan', 35165879, 'juan@gmail.com')  #imprime "Contacto añadido"
    agenda1.buscar_contacto('Cintia') #imprime todos los datos del contacto buscado
    agenda1.listar_contactos() #imprime los datos de los contactos añadidos
    agenda1.cerrar_agenda()   #imprime la agenda fue cerrada
         
if __name__=='__main__':
    __main__()


#No entiendo por qué no funciona ese while
# nom = input ('Ingrese el Nombre: ')
# while nom != ' ':
#     tel = input ('Ingrese el Teléfono: ')
#     email = input ('Ingrese el E-mail: ')
#     contacto1 = Contacto(nom, tel, email)
#     agenda1.anadir_contacto(contacto1)
#     nom = input ('Ingrese el Nombre: ')
# print(agenda1.lista_contactos)

#nom = input('Ingrese el nombre del contacto buscado:')