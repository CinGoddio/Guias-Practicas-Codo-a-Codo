#ACTIVIDAD PRÁCTICA UNIDAD 1

'''1) Escribe un programa muestre por pantalla “Hello World”.'''
#print('Hello World')

'''2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.'''
#print(3+5)

'''3) Escribe un programa que pida el nombre del usuario y escriba un texto que
diga “Hola nombreUsuario”'''
#nombreUsuario = input('Escriba su nombre: ')
#print('" Hola', (nombreUsuario),'"')

'''4)Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.'''
#num1 = int(input ('Ingrese un número: '))
#num2 = int(input ('Ingrese otro número: '))
#suma = num1 + num2
#print (suma)

'''5)Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.'''
#num1 = int(input ('Ingrese un número: '))
#num2 = int(input ('Ingrese otro número: '))
#if num1 > num2:
#    print((num1), 'es mayor que', (num2))
#elif num2 > num1:
#    print((num2), 'es mayor que', (num1))
#else:
#    print('Los números son iguales')

'''6)Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.'''
#num1 = int(input ('Ingrese un número: '))
#num2 = int(input ('Ingrese otro número: '))
#num3 = int(input ('Ingrese un último número: '))
#if num1 > num2 and num1 > num3:
#    print((num1), 'es el mayor de los números ingresados')
#elif num2 > num1 and num2 > num3:
#    print((num2), 'es el mayor de los números ingresados')
#elif num3 > num1 and num3 > num2:
#    print((num3), 'es el mayor de los números ingresados')

'''7) Escribe un programa que pida un número y diga si es divisible por 2'''
#num1 = int(input ('Ingrese un número: '))
#if num1%2 == 0:
#    print('El número es divisible por dos')
#else:
#    print('El número no es divisible por dos')

'''8)'''
'''9)'''
'''10)'''
'''11)'''

'''12) Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente'''

#nota= float(input("Ingrese una nota: "))
#while nota>10 or nota<1:
#    print("Error! La nota debe ser entre 1 y 10.")
#    nota= int(input("Ingrese una nota: "))
#if nota >=9:
#    print("Sobresaliente!")
#elif 7<= nota <9:
#    print("Notable!")
#elif 6<= nota <7:
#    print("Bien")
#elif 5<= nota <6:
#    print("Suficiente")
#elif 3<= nota <5:
#    print("Insuficiente")
#else:
#    print("Muy deficiente")

'''13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente forma:'''
#Primera alternativa saca da de StackOverflow
# #num=0
#while num < 30:
#    fila=num+1
#    cont=0
#    m=""
#    while(cont < fila):
#        m = m + str(num+1)
#        cont += 1
#    print(m)
#    num=num+1

#Respuesta del foro
#for i in range(1,31):
#    print(str(i)*i)

'''14) Haz un programa que escriba una pirámide inversa de los números del 1 al número que indique el usuario de 
la siguiente forma (suponiendo que indica 6):'''

# num = int(input('Ingrese un número (1 al 10): '))
# lista = []
# for i in range(1, num+1):
#     lista.append(str(i)*i) #Una vez guardada la piramide de nros, la imprimo en reversa
# for i in reversed(lista):
#     print(i)

'''15)Crear un programa que escriba los números del 1 al 500, y que indique cuales son múltiplos de 4 y de 9 y 
que cada 5 líneas muestre una línea horizontal'''
# for i in range(1,500+1):
#     if (i % 4 == 0):
#         print(i, 'es múltiplo de 4')
#     elif (i % 9 == 0):
#         print(i, 'es múltiplo de 9')
#     elif (i % 5 == 0):
#         print(i,'\n----------------')
#     else:
#         print(i)



