# Laboratorio de introduccion a programación seccion: 17
# 10/10/2023
# Fermando Motta Letona
# OBJETIVO: Crear funciones de conversion 
# ENTRADA: de Cm a m, Km, in, ft.
# PROCESOS "pedir al usario que selecciones una opción"
# SALIDA: conversion de moneda

import distan

cen=float(input("Ingrese medida en centimetros"))

opcion=""
while opcion != "5":
    print("Menù de opciones")
    print("1. CM a KM")
    print("2. CM a M")
    print("3. CM a IN")
    print("4. CM a FT")
    print("5. Salir")

    opcion= input("Seleccione alguna opción")
    if opcion == "1":
        km= round(distan.CMaKM(cen),2)
        print(cen, "cm, son:", km, "Km")
    elif opcion == "2":
        m= round(distan.CMaM(cen),2)
        print(cen, "cm, son:", m, "Km")
    elif opcion == "3":
        pu= round(distan.CMaIN(cen),2)
        print(cen, "cm, son:", pu, "in")
    elif opcion == "4":
        ft= round(distan.CMaFT(cen),2)
        print(cen, "cm, son:", ft, "ft")
    elif opcion == "8":
        print("Seleccionò salir")
        break
    else:
        print("ERROR, no seleccionó un numero valido")
