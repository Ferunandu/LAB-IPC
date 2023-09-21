# Laboratorio de introduccion a programación seccion: 17
# 21/09/2023
# Fermando Motta Letona
# OBJETIVO: Aprender a usar el For
# ENTRADA: datos del 1 al 10
# PROCESOS "pedir al usario que selecciones una opción"
# SALIDA: Que se salga cuando ella/el quiera

print("Fernando Motta")

while True:
    n2= int(input("Ingrese un numero de 1 a 10 "))

    if n2<=0:
        print("Error ingrese un numero valido")

    if n2>=10:
        print("Error ingrese un numero valido")

    else:
        for i in range(1,11):
            print(n2,"X",i, "=", i*n2)

    n3 = str(input("Desea volver a las tablas, ingrese si o no ")) 
    if n3 == "no":
    
        break




