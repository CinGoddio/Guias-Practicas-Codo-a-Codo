#ACTIVIDAD PRÁCTICA UNIDAD 2

'''1) Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si 
éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores 
lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la 
función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.'''

#FUNCIÓN
# def mayor_de_tres(num1, num2, num3):
#      if num1 > num2 >= num3:
#          rta = num1
#      elif num1 > num3 >= num2:
#          rta = num1
#      elif num2 > num1 >= num3:
#          rta = num2
#      elif num2 > num3 >= num1:
#          rta = num2
#      elif num3 > num1 >= num2:
#          rta = num3
#      elif num3 > num2 >= num1:
#          rta = num3
#      else: 
#          rta = -1
#      return rta
# # #PROGRAMA PRINCIPAL
# num1=int(input('Ingrese un número:'))
# num2=int(input('Ingrese otro número:'))
# num3=int(input('Ingrese un último número:'))
# if (mayor_de_tres(num1, num2, num3) == -1):
#    print('No hay un único mayor estricto')
# else:
#     print(mayor_de_tres(num1, num2, num3))

'''2)Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una 
fecha válida (día, mes, año). Devolver True o False según la fecha sea correcta o no. Realizar también un 
programa para verificar el comportamiento de la función.'''

# num1= int(input("Ingrese un número entero positivo:"))
# num2= int(input("Ingrese un número entero positivo:"))
# num3= int(input("Ingrese un número entero positivo:"))

# def fecha_valida(num1, num2, num3):
#     if (31 >= num1 >=1) and (num2==1 or num2==3 or num2==5 or num2==7 or num2==8 or num2==10 or num2==12) and (2022 >= num3 >=1):
#         rta = 'Fecha válida'
#     elif (30 >= num1 >=1) and (num2==4 or num2==6 or num2==9 or num2==11) and (2022 >= num3 >=1):
#         rta = 'Fecha válida'
#     elif (28 >= num1 >=1) and (num2==2) and (2022 >= num3 >=1):
#         rta = 'Fecha válida'
#     else: 
#         rta = 'Fecha no válida'
#     return rta  

# #PROGRAMA PRINCIPAL

# print(fecha_valida(num1, num2, num3))

'''3)Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero 
el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total 
de la compra y al dinero recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente 
como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes de $500, $100, 
$50, $20, $10, $5 y $1. Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la compra 
es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 
1 billete de $10 y 3 billetes de $1.'''

# #FUNCIÓN
# def convertir_cambio(total_compra, importe_recibido):
#     cambio = importe_recibido - total_compra
#     if importe_recibido - total_compra < 0:
#         print('Error. El dinero recibido es insuficiente para abonar la compra')
#     else:
#         b500 = cambio // 500   #división entera
#         cambio %= 500          #equivalente a cambio = cambio % 500 que devuelve el resto de la división
#         b100 = cambio // 100
#         cambio %= 100
#         b50 = cambio // 50
#         cambio %= 50
#         b20 = cambio // 20
#         cambio %= 20
#         b10 = cambio // 10
#         cambio %= 10
#         b5 = cambio // 5
#         cambio %= 5
#         b1 = cambio
#         return b500, b100, b50, b20, b10, b5, b1
# #PROGRAMA PRINCIPAL
# total_compra = 2120
# importe_recibido = 1000
# b500, b100, b50, b20, b10, b5, b1 = convertir_cambio(total_compra, importe_recibido)
# print(f'b500: {b500}, b100: {b100}, b50: {b50}, b20: {b20}, b10: {b10}, b5: {b5}, b2: {b1}')

'''4)Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones de 
asteriscos, donde la cantidad de filas se recibe como parámetro:'''
#FUNCIONES
# def cuadrado_asteriscos(cant_filas):
#     for i in range(1, cant_filas+1):
#         print ('**********') #str(cant_filas)*cant_filas

# def piramide_asteriscos(cant_filas):
#     for i in range(1, cant_filas+1):
#         print ('*'*i)

# #PROGRAMA PRINCIPAL
# cuadrado_asteriscos(2)
# piramide_asteriscos(4)

'''5)Crear una función lambda que devuelva el cuadrado de un valor recibido cómo parámetro. 
Desarrollar además un programa para verificar el comportamiento de la función.'''
# #FUNCIÓN
# cuadrado_numero = lambda x: x*x

# #PROGRAMA PRINCIPAL
# x = 4
# print(cuadrado_numero(x))

'''6)Crear una función lambda para comprobar si un número es par o impar. Desarrollar además 
un programa para verificar el comportamiento de la función.'''
# #FUNCIÓN
# es_par = lambda x : x % 2 == 0
# #PROGRAMA PRINCIPAL
# x = 5
# print(es_par(x))

'''7)Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.'''
#FUNCIÓN
# def cuadrados_lista(N):
#     lista = list (range (1,N+1))
#     for i in range(len(lista)):
#         lista[i]**=2    
#     return lista

# #PROGRAMA PRINCIPAL  
# N = 5
# print(cuadrados_lista(N)[-10:]) #imprime los últimos diez valores de la lista

'''8)Eliminar de una lista de palabras que se encuentren en una segunda lista. Imprimir la lista 
original, la lista de palabras a eliminar y la lista resultante.'''

# lista_original = ['UNO', ['DOS', 'TRES'], 'CUATRO', 'CINCO']

# print('Lista original:', lista_original)
# print('Palabras -lista- a eliminar:', lista_original[1])
# lista_original.pop(1) #lista_original.pop(1) elimina el elemento de la posición 1 que es la lista ['DOS', 'TRES']
# print('Lista resultante:', lista_original) #imprime la lista original luego de haber eliminado el elemento 
# de la posición 1

# Otra forma (ahorrando un paso ya que en el mismo paso que elimino, imprimo lo que elimino):
# lista = [10, 12, 15]
# print(lista)
# print(lista.pop(1))
# print(lista)

'''9)Escribir una función que reciba una lista como parámetro y devuelva True si la lista está 
ordenada en forma ascendente o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna 
True y ordenada(['b', 'a']) retorna False. Desarrollar además un programa para verificar el 
comportamiento de la función.'''
'''SIEMPRE DA FALSO'''
#FUNCIÓN
# def lista_ordenada(lista):
#No funciona porque el lista.sort() no puede asignarse al comparativo y hacerlo ejecutar la 
# función, se debe primero hacer ejecutar la función y luego asignarlo al compartaivo como lo hice más abajo
#     if lista==lista.sort(): #return lista == lista.sort() es una alternativa más simple
#         rta = True
#     else:
#         rta = False
#     return rta

#Otra forma...FUNCIONA
def lista_ordenada(lista):
    ordenada = sorted(lista)
    return lista == ordenada #return true if lista == ordenada; otherwise return false


# #PROGRAMA PRINCIPAL
lista = [2, 3, 5]
print(lista_ordenada(lista))


'''10)Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas 
auxiliares ni rebanadas. Escribir además un programa que permita verificar su funcionamiento.'''

# def es_capicua(cadena):
#     for i in range(len(cadena)-1):
#         if cadena[i] == cadena[-1-i]:
#             rta = True
#         else:
#             rta = False
#         return rta

# #PROGRAMA PRINCIPAL

# cadena = 'anana'
# print(cadena[-2])
# print(es_capicua(cadena))

'''11)Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.'''
#FUNCIÓN
# def cadena_centrada(cadena):
#     longitud = len(cadena)
#     caracteres_al_comienzo = int((80 - longitud)/2)
#     print(" "*caracteres_al_comienzo, cadena)

# #PROGRAMA PRINCIPAL
# cadena = input('Ingrese una cadena de caracteres:')
# cadena_centrada(cadena)

'''12)Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva 
una cadena de caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para (12, 10,17) 
devuelve “12 de Octubre de 2017”. Escribir también un programa para verificar su comportamiento.'''
#FUNCIÓN
#Funciona pero no cumple la consigna de usar TUPLA. HECHO DE MANERA CORRECA MÁS ABAJO
# def fecha_extendida(dia, mes, anio):
#     if mes==1:
#         rta = f'{dia} de Enero de {anio}'
#     elif mes==2:
#         rta = f'{dia} de Febrero de {anio}'
#     elif mes==3:
#         rta = f'{dia} de Marzo de {anio}'
#     elif mes==4:
#         rta = f'{dia} de Abril de {anio}'
#     elif mes==5:
#         rta = f'{dia} de Mayo de {anio}'
#     elif mes==6:
#         rta = f'{dia} de Junio de {anio}'
#     elif mes==7:
#         rta = f'{dia} de Julio de {anio}'
#     elif mes==8:
#         rta = f'{dia} de Agosto de {anio}'
#     elif mes==9:
#         rta = f'{dia} de Septiembre de {anio}'
#     elif mes==10:
#         rta = f'{dia} de Octubre de {anio}'
#     elif mes==11:
#         rta = f'{dia} de Noviembre de {anio}'
#     elif mes==12:
#         rta = f'{dia} de Diciembre de {anio}'
#     return rta

# #PROGRAMA PRINCIPAL
# dia = 16
# mes = 11
# anio = 2022
# print(fecha_extendida(dia, mes, anio))

#Forma CORRECTA:
# def fecha_extendida2(tupla):
#     dia, mes, anio = tupla
#     if mes==1:
#         rta = 'Enero'
#     elif mes==2:
#         rta = 'Febrero'
#     elif mes==3:
#         rta = 'Marzo'
#     elif mes==4:
#         rta = 'Abril'
#     elif mes==5:
#         rta = 'Mayo'
#     elif mes==6:
#         rta = 'Junio'
#     elif mes==7:
#         rta = 'Julio'  #y así seguimos...
#     return f'{dia} de {rta} de {anio}'

# #PROGRAMA PRINCIPAL

# tupla = (17, 11, 1983)
# print(fecha_extendida2(tupla))

'''13)Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, 
dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.'''

# frase_ingresada = input('Ingrese una frase: ')
# lista = frase_ingresada.split()
# conjunto = (set(lista))
# lista_sin_repetir = list(conjunto)
# lista_sin_repetir.sort(key=len)

# # print(frase_ingresada)
# # print(lista)
# # print(conjunto)
# print(lista_sin_repetir)

'''14) Desarrollar una función eliminar_claves() que reciba como parámetros un diccionario y una lista 
de claves. La función debe eliminar del diccionario todas las claves contenidas en la lista, devolviendo 
el diccionario modificado y un valor de verdad que indique si la operación fue exitosa. Desarrollar también 
un programa para verificar su comportamiento.'''
'''SEGUIR'''
