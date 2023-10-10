# Laboratorio de introduccion a programación seccion: 17
# 10/10/2023
# Fermando Motta Letona
# OBJETIVO: Crear funciones de conversion 
# ENTRADA: de Cm a m, Km, in, ft.
# PROCESOS "pedir al usario que selecciones una opción"
# SALIDA: conversion de moneda

def CMaKM(centi):
    resul= centi/100000
    return resul

def CMaM(centi):
    resul= centi/100
    return resul

def CMaIN(centi):
    resul= centi/2.54
    return resul

def CMaFT(centi):
    resul= centi/30.48
    return resul