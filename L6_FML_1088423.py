# Laboratorio de introduccion a programaciòn seccion: 17
# 12 /09/2023
# Fermando Motta Letona
# OBJETIVO: nombrar y decir que dia es
# ENTRADA: numero indicador de dias
# PROCESOS "Determinar los dias en numero y si no esta dentro del rango marcar error"
# SALIDA: El dia de hoy es:

print("Ejercicio 2")

d1= int(input("Ingrese numero de 1 a 7 de acuerdo al dia"))

if d1== 1:
    print("Hoy es lunes")

if d1== 2:
    print("Hoy es Martes")

if d1== 3:
    print("Hoy es miercoles")

if d1== 4:
    print("Hoy es jueves")

if d1== 5:
    print("Hoy es viernes")

if d1== 6:
    print("Hoy es sabado")

if d1== 7:
    print("Hoy es domingo")

elif d1<1 or d1>7:
    print("ERROR: ingrese numero entre 1-7")