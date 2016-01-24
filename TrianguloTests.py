import unittest

from Triangulo import Triangulo


class TrianguloTestCases(unittest.TestCase):

    def setUp(self):
        self.triangulo = Triangulo()

    def tearDown(self):
        self.triangulo = None

    def test_espera_true_quando_lados_do_triangulo_sao_validos(self):
        self.assertEqual(self.triangulo.is_triangulo(10, 8, 6), True)

    def test_espera_false_quando_lados_do_triangulo_sao_invalidos(self):
        self.assertEqual(self.triangulo.is_triangulo(-1, 0, 42), False)


if __name__ == '__main__':
    unittest.main()
