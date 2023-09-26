# Laboratorio de introduccion a programación seccion: 17
# 26/09/2023
# Fermando Motta Letona
# OBJETIVO: 
# ENTRADA: 
# PROCESOS ""
# SALIDA: 

import math




opcion=""

conta=1
while opcion != "3":
    print("Menù de opciones")
    print("1. Factoriual")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")
    opcion= input("Seleccione alguna opciòn")

    if opcion == "1":
        print("Ha seleccionado Factorial")
        a1= int(input("Ingrese un numero entero"))
        
        while conta<=a1:
            print(a1,"*",a1-conta,"*",(a1-conta)-1,"*",((a1-conta)-1)-1)
            conta = conta +1 

            if a1-conta == 0:
                break


    elif opcion == "2":
        print("El resultado para la sucesion de Fibonacci de", a1, "=", )
    elif opcion == "3":
        break
