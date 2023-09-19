# Introducción a la programacion (lab) s17
# 19/09/2023
# Fernando Motta Letona 1088423
# Objetivo: Uso y manejo de variables Sting e input
# Entrada: Valores ingresados y operados jerarquicamente
# procesos: pedir numeros enteros y realizar las operaciones necesarias.
# Salida: Resultados numericos.

# ejercicio 3

a1 = int(input("Ingrese un número "))
b2 = int(input("Ingrese otro número "))
c3 = int(input("Ingrese un último número "))

print(a1, "x", b2, "+", c3, "=", (a1 * b2) + c3)
print(a1, "x (", b2, "+", c3, ") =", a1 * (b2 + c3))
print(a1, "/", b2, "x", c3, "=", a1 / (b2 * c3))
print("3(", a1, ") + 2(", b2, ")/", c3, "^2 =" , ((a1 * 3) + (b2 * 2)) / (c3 ** 2) )