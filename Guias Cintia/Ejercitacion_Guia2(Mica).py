"""
# 1) ME APARECE UN NONE AL FINAL EN LA TERMINAL!!! Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.

a = int(input("Escriba un número positivo:"))
b = int(input("Escriba un número positivo:"))
c = int(input("Escriba un número positivo:"))
def mayor_tres(a, b, c):
    if a == b:
        return print("El máximo extricto no existe")
    elif b == c:
        return print("El máximo extricto no existe")
    elif a == c:
        return print("El máximo extricto no existe")
    else:
        return print("El máximo es:",max(a,b,c))
    
print(mayor_tres(a,b,c))


#2) Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha válida (día, mes, año). Devolver True o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.

num1= int(input("Ingrese un número entero positivo:"))
num2= int(input("Ingrese un número entero positivo:"))
num3= int(input("Ingrese un número entero positivo:"))

def fecha_valida(num1, num2, num3):
    if (31 >= num1 >=1) and (num2==1 or num2==3 or num2==5 or num2==7 or num2==8 or num2==10 or num2==1 or num2==12) and (2022 >= num3 >=1):
        return True
    elif (30 >= num1 >=1) and (num2==4 or num2==6 or num2==9 or num2==11) and (2022 >= num3 >=1):
        return True
    elif (28 >= num1 >=1) and (num2==2) and (2022 >= num3 >=1):
        return True
    else:
        return False        

print(fecha_valida(num1, num2, num3))

# 3) Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.

tot_compra = int(input("Ingrese el monto total de la venta:"))
dinero_recibido = int(input("Ingrese el monto de dinero que le entrego el cliente:"))

def cambio_a_entregar():
    if dinero_recibido-tot_compra < 0:
        return("Error dinero insuficiente")
    else:
        b500 = (dinero_recibido - tot_compra)// 500
        cambio = (dinero_recibido-tot_compra) % 500
        b100 = cambio // 100
        cambio = cambio % 100
        b50 = cambio // 50
        cambio = cambio %50
        b20 = cambio // 20
        cambio = cambio % 20    
        b10 = cambio // 10
        cambio = cambio % 10
        b5 = cambio // 5
        cambio = cambio % 5
        b1 = cambio
        return("Su vuelto es: $",dinero_recibido - tot_compra, b500,"billetes de $500", b100,"billetes de $100", b50,"billetes de $50", b20,"billetes de $20", b10,"billetes de $10", cambio,"billetes de $1") 

print(cambio_a_entregar())


#4) DE NUEVO ME APARECE EL NONE AL FINAL Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:

def asteriscos(cant_filas):
    for i in range (0, cant_filas):
        print ("**********")

print(asteriscos(5))

def asteriscos_piramide(canto_filas1):
    for i in range (1, canto_filas1+1):
        print ("**"*i)
        
print(asteriscos_piramide(5))

#5) Crear una función lambda que devuelva el cuadrado de un valor recibido cómo parámetro. Desarrollar además un programa para verificar el comportamiento de la función.

cuadrado = lambda x : x **2
print(cuadrado(4))

#6) Crear una función lambda para comprobar si un número es par o impar. Desarrollar además un programa para verificar el comportamiento de la función.

par = lambda x : x % 2 == 0
print(par(5))

#7) Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.

N = int(input("Ingrese un número:"))

def cuadrados(N):
    lista = list (range(1,N+1))
    for i in range(len(lista)):
        lista [i]**=2
    return lista

print(cuadrados(N)[-10:])


#8) Eliminar de una lista de palabras que se encuentren en una segunda lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", ["Sábado", "Domingo"]]
print(dias_semana)
print(dias_semana[5])
dias_semana.pop()
print(dias_semana)

#9) Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar además un programa para verificar el comportamiento de la función.
#PROBE 3 METHODOS DIFERENTES TODOS ME DAN FALSE
lista=[1,5,3]

def esta_ordenada(lista):
    for i in range(1,len(lista)-1):
        if lista[i] < lista[i-1]:
            return False
        else:
            return True
print(esta_ordenada(lista))



#10) Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita verificar su funcionamiento.

cadena ="Micaela"
print(len(cadena))

def es_capicua(cadena):
    for i in range(len(cadena)-1):
        if cadena[i] == cadena[-1-i]:
            rta = True
        else:
            rta = False
    return rta

    
print(es_capicua(cadena)) 


#11) Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.

cadena = input("Ingrese una cadena de caracteres:")

def cadena_centrada(cadena):
    long = len(cadena)
    caract_al_comienzo = int((80 - long)/2)
    print(" "*caract_al_comienzo,cadena)
    
print(cadena_centrada(cadena))


#12) Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de Octubre de 2017”. Escribir también un programa para verificar su comportamiento.

dia= input("Ingrese un día:")
mes= input("Ingrese un mes:")
ano= input("Ingrese un año:")

tupla = (dia, mes, ano)

def funcion_extendida(dia,mes,ano):
    if mes == 1:
        rta = "Enero"
    elif mes == 2:
        rta = "Febrero"
    elif mes == 3:
        rta = "Marzo"
    else:
        rta = "Diciembre"
    return dia+" de "+rta+" de "+ano

print(funcion_extendida(dia,mes,ano))



#13) Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.

frase = input("Ingrese una frase:")
lista = frase.split()
conjunto = set(lista)
print(conjunto)
# print(sorted(conjunto)) lo ordena alfabeticamente
lista_sin_repes = list(conjunto)
lista_sin_repes.sort(key=len)
print(lista_sin_repes)

#14) Desarrollar una función eliminar_claves() que reciba como parámetros un diccionario y una lista de claves. La función debe eliminar del diccionario todas las claves contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad que indique si la operación fue exitosa. Desarrollar también un programa para verificar su comportamiento.

#dicc = dict(nombre="Micaela", edad=41, sexo="Femenino", Civil="Casada", Fecha_nac=(30,12,1980))
dicc = { 
        "nombre":"Micaela", 
        "edad":41,
        "sexo":"Femenino", 
        "Civil":"Casada", 
        "Fecha_nac":(30,12,1980)
}
lista_claves_eliminar = ["sexo", "Civil"]

def eliminar_claves(diccionario,lista):
    for elem in lista:
        diccionario.pop(elem)
    return print(diccionario)
          
print(eliminar_claves(dicc, lista_claves_eliminar))
"""
#15) Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres dados, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma. Escribir una función utilizando rebanadas.

cadena = "Micaela"
posicion = 2
cantidad = 2
print(cadena)

def eliminar_subcadena(cadena,posicion,cantidad):
    cadena_elim = slice(posicion,posicion+cantidad)
    print(cadena[cadena_elim])
    print(type(cadena_elim)) #Me da class slice, no se como cambiarla a str
    return cadena.strip(cadena_elim) 
#cadena.replace(cadena_elim,"")
print(eliminar_subcadena(cadena,posicion,cantidad))           

         


