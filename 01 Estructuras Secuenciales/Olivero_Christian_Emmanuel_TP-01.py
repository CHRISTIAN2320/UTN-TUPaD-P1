# Actividades
#%%
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola mundo")
#%%
# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

Nombre=input("Ingrese su Nombre: ")
print(f"Hola {Nombre}!")

#%%
# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla

Nombre=input("Ingrese su Nombre: ")
Apellido= input("Ingrese su Apellido: ")
Edad=input("Ingrese su Edad: ")
Lugar_Residencia=input("Ingrese lugar de residencia: ")
print(f"Soy {Nombre} {Apellido}, tengo {Edad} años y vivo en {Lugar_Residencia}")

#%%
#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
import math
radio=int(input("Ingrese el radio de un circulo: "))
area=2*math.pi*radio**2
perimetro=2*math.pi*radio
print(f"El area de un circulo es: {area} y el perimetro es: {perimetro}")

#%%
# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos=int(input("ingrese una cantidad de segundos: "))
horas=segundos/60/60
print(f"la cantidad de horas son: {horas}")
#%%
# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
n=int(input("Ingrese un numero: "))
print( n,"x 1 = " ,(n*1))
print( n,"x 2 = ", (n*2))
print( n,"x 3 = ", (n*3))
print( n,"x 4 = ", (n*4))
print( n,"x 5 = ", (n*5))
print( n,"x 6 = ", (n*6))
print( n,"x 7 = ", (n*7))
print( n,"x 8 = ", (n*8))
print( n,"x 9 = ", (n*9))
print( n,"x 10 =",(n*10))
#%%
# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
n1=int(input("Ingrese el primero numero distinto de cero: "))
n2=int(input("Ingrese el segundo numero distinto de cero: "))
print("suma: ",n1+n2)
print("resta: ",n1-n2)
print("multiplicacion: ",n1*n2)
print("division: ",n1/n2)
#%%
# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:

altura=float(input("Ingrese su altura: "))
peso=float(input("Ingrese su peso"))
print("Su indice de masa corporal es: ",(peso/altura**2))
# %%
#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
TempC=float(input("Ingrese temperatura en Grados Celcius: "))
print("La temperatura en Grados Fahrenheit es: ",(9/5*TempC+32))
#%%
# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números
n1=int(input("Ingrese primer número: "))
n2=int(input("Ingrese segundo número: "))
n3=int(input("Ingrese tercer número: "))
suma=n1+n2+n3
print("El promedio de los tres numeros es:", suma/3)
