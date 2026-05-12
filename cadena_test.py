# -*- coding: utf-8 -*-
# Indicamos la codificación del archivo para evitar problemas con caracteres especiales

import unittest
import random
import string
from cadena import cadena_mas_larga
# Importamos la función que queremos probar desde el archivo principal

class TestCadenaMasLarga(unittest.TestCase):
   #Señalamos con unittest

    def test_ejemplo_enunciado(self):
        #Caso del enunciado
        lista = ["a", "ab", "abc", "dddd", "abcd"]
        self.assertEqual(cadena_mas_larga(lista), "abcd")

    def test_lista_vacia(self):
        #Lista vacía
        self.assertEqual(cadena_mas_larga([]), "")

    def test_tipo_incorrecto(self):
        #tipo incorrecto (es un string)
        with self.assertRaises(TypeError):
            cadena_mas_larga("hola")

    def test_elementos_no_validos(self):
        #tipo incorrecto 2 (lista pero no es cadena)
        with self.assertRaises(TypeError):
            cadena_mas_larga(["hola", 3])

    def test_datos_aleatorios(self):
        #test automatizado con chars aleatorios
        for _ in range(5):  # Repetimos la prueba varias veces
            lista = []

            # Generamos varias palabras aleatorias
            for _ in range(3):
                palabra = ''.join(
                    random.choice(string.ascii_lowercase) for _ in range(5)
                )
                lista.append(palabra)

            # Ejecutamos la función con los datos generados
            resultado = cadena_mas_larga(lista)

            # Comprobamos que el resultado pertenece a la lista original
            self.assertIn(resultado, lista)


# Punto de entrada para ejecutar los tests desde consola
if __name__ == "__main__":
    unittest.main()
