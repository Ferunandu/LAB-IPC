# Laboratorio de introduccion a programaciòn seccion: 17
# 13/11/2023
# Fermando Motta Letona
# OBJETIVO: Hacer un BattleShift funcional
# ENTRADA: Coordenadas de barcos y disparo
# PROCESOS: "Ingreso de coordenadas de barcos, ingreso de coordenadas de disparo"
# SALIDA: disparo exitoso o no

import random

class base:
    def __init__(self):
        self.base = [[' ' for _ in range(10)] for _ in range(10)]

    def imprimir_base(self):
        print("   1 2 3 4 5 6 7 8 9 10")
        letras = "ABCDEFGHIJ"
        for i in range(10):
            fila = " ".join(self.base[i])
            print(f"{letras[i]} |{fila}|")

    def v_coor(self, fila, columna):
        return 0 <= fila < 10 and 0 <= columna < 10

    def colocar_barco(self, fila, columna, orientacion, longitud):
        if orientacion == 'horizontal':
            if columna + longitud <= 10:
                for i in range(longitud):
                    if self.base[fila][columna + i] != ' ':
                        return False
                for i in range(longitud):
                    self.base[fila][columna + i] = 'O'
                return True
        elif orientacion == 'vertical':
            if fila + longitud <= 10:
                for i in range(longitud):
                    if self.base[fila + i][columna] != ' ':
                        return False
                for i in range(longitud):
                    self.base[fila + i][columna] = 'O'
                return True
        return False

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.base = base()
        self.b_pequeno = 3
        self.b_grande = 2
        self.b_hundidos = 0

    def colocar_barcos(self):
        print(f"{self.nombre}, coloca tus barcos:")
        while self.b_pequeno > 0:
            self.base.imprimir_base()
            fila, columna, orientacion = self.o_coordenadas()
            if self.base.colocar_barco(fila, columna, orientacion, 3):
                self.b_pequeno -= 1
            else:
                print("No se puede colocar el barco en esas coordenadas. Inténtalo de nuevo.")
        while self.b_grande > 0:
            self.base.imprimir_base()
            fila, columna, orientacion = self.o_coordenadas()
            if self.base.colocar_barco(fila, columna, orientacion, 5):
                self.b_grande -= 1
            else:
                print("No se puede colocar el barco en esas coordenadas. Inténtalo de nuevo.")

    def o_coordenadas(self):
        fila = input(f"{self.nombre}, ingresa la fila (A-J): ").upper()
        while fila not in "ABCDEFGHIJ":
            fila = input("Por favor, ingresa una fila válida (A-J): ").upper()
        columna = int(input("Ingresa la columna (1-10): ")) - 1
        orientacion = input("Ingresa la orientación (horizontal o vertical): ").lower()
        while orientacion not in ["horizontal", "vertical"]:
            orientacion = input("Por favor, ingresa una orientación válida (horizontal o vertical): ").lower()
        fila_numero = ord(fila) - ord('A')
        return fila_numero, columna, orientacion

def disparar(oponente, jugador):
    print(f"{jugador.nombre}, es tu turno de disparar:")
    oponente.base.imprimir_base()

    fila, columna, orientacion = jugador.o_coordenadas()

    if oponente.base.base[fila][columna] == 'O':
        print("¡Acertaste! Has alcanzado un barco.")
        oponente.base.base[fila][columna] = 'X'
        oponente.b_hundidos += 1
        if oponente.b_hundidos == 5:
            print(f"{jugador.nombre} ha ganado. ¡Felicidades!")
            return True
    else:
        print("Disparo fallido.")
        oponente.base.base[fila][columna] = '-'
    return False

def main():
    print("¡Bienvenido al juego de Batalla Naval!")

    nombre_jugador1 = input("Jugador 1, ingresa tu nombre: ")
    nombre_jugador2 = input("Jugador 2, ingresa tu nombre: ")

    jugador1 = Jugador(nombre_jugador1)
    jugador2 = Jugador(nombre_jugador2)

    jugador1.colocar_barcos()
    jugador2.colocar_barcos()

    turno = 1
    jugador_actual = jugador1
    oponente = jugador2

    while True:
        if disparar(oponente, jugador_actual):
            break
        input("Presiona Enter para continuar...")
        turno = 3 - turno
        jugador_actual, oponente = oponente, jugador_actual

if __name__ == "__main__":
    main()