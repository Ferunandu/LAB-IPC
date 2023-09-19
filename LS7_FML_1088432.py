# Laboratorio de introduccion a programaciòn seccion: 17
# 19 /09/2023
# Fermando Motta Letona
# OBJETIVO: Calcular con operacion aritmeticas los datos ingresados
# ENTRADA: Numeros y operaciones aritmeticas
# PROCESOS: "usaando concionales y funciones aritmeticas"
# SALIDA:resultados operacionales

n1= int(input("Ingrese cualquier numero"))
n2= int(input("Ingrese otro numero cualquiera"))

# Parte 2 del ejercicio
opcion=""
while opcion != "8":
    print("Menù de opciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicaciòn")
    print("4. Cociente")
    print("5. Divisiòn")
    print("6. Porcentaje")
    print("7. Exponente")
    print("8. Salir")
    opcion= input("Seleccione alguna opciòn")
    if opcion == "1":
        print("Seleccionò La suma")
        print(n1,"+", n2 ,"=", n1 + n2)
    elif opcion == "2":
        print("Seleccionò La resta")
        print(n1,"-", n2 ,"=",n1 - n2)
    elif opcion == "3":
        print("Seleccionò La multiplicaciòn")
        print(n1,"x", n2 ,"=", n1 * n2)
    elif opcion == "4":
        print("Seleccionò el cociente")
        print(n1,"//", n2 ,"=", n1 // n2)
    elif opcion == "5":
        print("Seleccionò la division")
        print(n1,"/", n2 ,"=", n1 / n2)
    elif opcion == "6":
        print("Seleccionò el porcentaje")
        print(n1,"%", n2 ,"=", n1 % n2)
    elif opcion == "7":
        print("Seleccionò la exponenciaciòn")
        print(n1,"**", n2 ,"=", n1 ** n2)
    elif opcion == "8":
        print("Seleccionò salir")
    
    else:
        print("ERROR, seleccione un numero valido")

