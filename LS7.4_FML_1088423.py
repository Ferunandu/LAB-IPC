# Introducción a la programacion (lab) s17
# 19/09/2023
# Fernando Motta Letona 1088423
# Objetivo: Uso y manejo de variables Sting e input
# Entrada: Valores ingresados y operados jerarquicamente
# procesos: pedir numeros enteros y realizar las operaciones necesarias.
# Salida: Resultados numericos.

# ejercicio 3

import math

a1 = int(input("Ingrese un número "))
b2 = int(input("Ingrese otro número "))
c3 = int(input("Ingrese un último número "))

opcion=""
while opcion != "6":
    print("Menù de opciones")
    print("1. a x b +c")
    print("2. a x (b + c)")
    print("3. a / (b x c)")
    print("4. (3a + 2b) / c^2 ")
    print("5. Ecuación cuadratica")
    print("6. Salir")

    opcion= input("Seleccione alguna opciòn")
    if opcion == "1":
        print(a1, "x", b2, "+", c3, "=", (a1 * b2) + c3)
    elif opcion == "2":
        print(a1, "x (", b2, "+", c3, ") =", a1 * (b2 + c3))
    elif opcion == "3":
        print(a1, "/", b2, "x", c3, "=", a1 / (b2 * c3))
    elif opcion == "4":
        print("3(", a1, ") + 2(", b2, ")/", c3, "^2 =" , ((a1 * 3) + (b2 * 2)) / (c3 ** 2) )
    elif opcion == "5":
        if a1 != 0 and ((b2**2) - (4 * a1 * b2)) >= 0:
            print( "Un resultado de la cuadratica es:", (-b2 + math.sqrt((b2**2)-(4*a1*c3)))/(2*a1) )
            print( "Otro resultado de la cuadratica es:", (-b2 - math.sqrt((b2**2)-(4*a1*c3)))/(2*a1) )
    elif opcion == "8":
        print("Seleccionò salir")

    else:
        print("ERROR, no seleccionó un numero valido")
