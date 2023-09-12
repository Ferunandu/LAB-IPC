# Laboratorio de introduccion a programaciòn seccion: 17
# 12 /09/2023
# Fermando Motta Letona
# OBJETIVO: comparar numeros y marcar error si no es numero.
# ENTRADA: Numero entero
# PROCESOS "Determinaciòn de numero positvo o negativo y marcar error si no se pone algun numero"
# SALIDA: Resultado

print("Ejercicio 1")
n1= int(input("Ingrese numero entero   "))


if n1>0:
    print(n1, " es positivo")
if n1<0:
    print(n1, " es negativo")
if n1==0:
    print(n1, " es cero")


