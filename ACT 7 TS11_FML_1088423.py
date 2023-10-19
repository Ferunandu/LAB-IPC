# Introducción a la programacion s17
# 19/10/2023
# Fernando Motta Letona 1088423 
# Objetivo:  
# Entrada: 
# procesos:
# Salida: 

pal=str(input("ingrese una palabra"))

tres_letras= pal[:3]
print("las primeras tres letras son:", tres_letras)

new_pal=tres_letras

texto=str(input("Ingresa un texto"))

modi=""
for caracter in texto:
    if caracter == "o" or caracter == "O":
        modi += "x"
    else:
        modi += caracter

print("Ya modificado es:", modi)
