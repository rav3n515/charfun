# charfun.py

# Definimos esPalindromo
def esPalindromo(frase):
    frase = ''.join(filter(str.isalnum, frase)).lower()
    return frase == frase[::-1]

# Pedimos al usuario que introduzca una frase y mostramos el resultado si es un palíndromo o no
if __name__ == "__main__":
    frase = input("Introduce una frase: ")
    print("Es un palíndromo." if esPalindromo(frase) else "No es un palíndromo.")

# Importamos la librería unittest
import unittest

# Creamos la clase de pruebas TestPalindromo
class TestPalindromo(unittest.TestCase):

    # Definimos tipo de testeo para probar si "Anita lava la tina" es palíndromo
    def test_anita_lava_la_tina(self):
        resultado = esPalindromo("Anita lava la tina")
        self.assertEqual(resultado, True)

    # Prueba una frase que no es un palíndromo
    def test_no_palindromo(self):
        resultado = esPalindromo("Esto no es un palíndromo")
        self.assertEqual(resultado, False)

    # Prueba una cadena vacía
    def test_cadena_vacia(self):
        resultado = esPalindromo("")
        self.assertEqual(resultado, True)

    # Prueba con un solo carácter
    def test_un_solo_caracter(self):
        resultado = esPalindromo("a")
        self.assertEqual(resultado, True)

    # Prueba solo números
    def test_con_numeros(self):
        resultado = esPalindromo("12321")
        self.assertEqual(resultado, True)
        resultado = esPalindromo("12345")
        self.assertEqual(resultado, False)

    # Prueba con caracteres especiales
    def test_con_caracteres_especiales(self):
        resultado = esPalindromo("@Anita! lava, la tina@")
        self.assertEqual(resultado, True)

# Ejecutamos las pruebas
if __name__ == "__main__":
    unittest.main()

