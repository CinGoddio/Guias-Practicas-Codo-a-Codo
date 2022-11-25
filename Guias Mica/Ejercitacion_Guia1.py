'''
# 1)Escribe un programa muestre por pantalla “Hello World”.
print("Hello World")

# 2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
print (3+5)

# 3) Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”
nombre = input("Ingrese su nombre de usuario:")
print("Hola",nombre)

# 4) Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.
a=int(input("Ingrese un número:"))
b=int(input("Ingrese otro número:"))
print(a+b)

# 5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
c=int(input("Ingrese un número:"))
d=int(input("Ingrese otro número:"))
if c > d:
    print("El mayor es:",c)
elif d > c:
    print("El mayor es:",d)
else:
    print("Los números ingresados son iguales")

# 6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.
num1=int(input("Ingrese un número:"))
num2=int(input("Ingrese otro número:"))
num3=int(input("Ingrese otro número:"))

if num1>num2 and num1>num3:
    print("El mayor es:",num1)
elif num2>num1 and num2>num3:
    print("El mayor es:",num2)
else:
    print("El mayor es:",num3)

# 7) Escribe un programa que pida un número y diga si es divisible por 2
num4 = int(input("Ingrese un número:"))
div2=num4%2
if div2 == 0:
    print("El número ",num4," es divisible por 2")
else:
    print("El número ",num4," NO es divisible por 2")

# 8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)
# 9) NO ME SALIO!! Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay que decir todos por los que es divisible)

num5 = int(input("Ingrese un número:"))
div2=num5%2
div3=num5%3
div5=num5%5
div7=num5%7
#if div2==0 or div3==0 or div5==0 or div7==0:
#   print("Es divisible")
#else:
#   print("El número ingresado no es divisible por 2,3,5 o 7")

# 10) Escribir un programa que escriba en pantalla los divisores de un número dado
num6 = int(input("Ingrese un número:"))
cont=1
while cont<=num6:
    if num6%cont==0:
        print(num6,"Es divisible por: ",cont)
    cont=cont+1

# 11) NO ME SALIO!!! Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)
num7 = int(input("Ingrese un número:"))
cont=2
while cont<num7:
    if num7%cont == 0:   
        print("NO es primo")
        cont = num7  
    else:
        cont=cont+1
    print("Es primo")
    
# 12) Pide una nota (número). Muestra la calificación según la nota: 0-3: Muy deficiente, 3-5: Insuficiente, 5-6: Suficiente, 6-7: Bien, 7-9: Notable, 9-10: Sobresaliente

nota = float(input("Ingrese un la nota:"))

while nota>10 or nota<=0:
    print("Error! La nota debe ser entre 1 y 10.")
    nota= float(input("Ingrese una nota: "))

if nota >=0 and nota <3:
    print("Muy deficiente")
elif nota >=3 and nota <5:
    print("Insuficiente")
elif nota >=5 and nota <6:
    print("Suficiente")
elif nota >=6 and nota <7:
    print("Bien")
elif nota >=7 and nota <9:
    print("Notable")
elif nota >=9 and nota <10:        
    print("Sobresaliente")
else:
    print("Error, vuelva a cargar la nota la misma debe estar entre 0 y 10")   


# 13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente forma:
for i in range(1,31):
    print(str(i)*i)

# 14) Haz un programa que escriba una pirámide inversa de los números del 1 al número que indique el usuario de la siguiente forma (suponiendo que indica 6):

for i in range(0,6):
    print(str(6-i)*(6-i))
'''
# 15) NO ME SALEN LAS LINEAS PUNTEADAS CADA 5 SI ES MULTIPLO DE 4. Crear un programa que escriba los números del 1 al 500, y que indique cuales son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal.

#\n es un salto de página, si lo ponés en el divisor de 5 te queda como lo pide el ejercicio.
for i in range(1,501):
    
    if i%4==0:
        print(i,"(Es múltiplo de 4)")
    elif i%9==0:
        print(i,"(Es múltiplo de 9)")
    else:
        print(i)