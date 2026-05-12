# -*- coding: utf-8 -*-
"""
Script que permite obtener la cadena más larga de una lista de cadenas.
Incluye validación de entradas y control de errores para garantizar
un comportamiento seguro ante valores no válidos.
"""
def cadena_mas_larga(lista):
    # La entrada debe ser una lista
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista")

    # Caso lista vacía
    if lista == []:
        return ""

    # Todos los elementos deben ser cadenas
    for e in lista:
        if not isinstance(e, str):
            raise TypeError("La lista solo puede contener cadenas")

    mas_larga = ""

    # Ordenamos para controlar empates alfabéticos
    for e in sorted(lista):
        if len(e) > len(mas_larga):
            mas_larga = e

    return mas_larga


if __name__ == "__main__":
    palabras = []

    # Pedimos 5 palabras al usuario
    for _ in range(5):
        palabras.append(input("Introduce una palabra: "))

    # Controlamos posibles errores de tipo
    try:
        print(cadena_mas_larga(palabras))
    except TypeError as e:
        print("Error:", e)