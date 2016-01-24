import unittest

from Triangulo import Triangulo


class TrianguloTestCases(unittest.TestCase):

    def setUp(self):
        self.triangulo = Triangulo()

    def tearDown(self):
        self.triangulo = None

    def test_is_triangulo_espera_true_quando_lados_sao_validos(self):
        self.assertEqual(self.triangulo.is_triangulo(10, 8, 6), True)

    def test_is_triangulo_espera_false_quando_lados_sao_invalidos(self):
        self.assertEqual(self.triangulo.is_triangulo(-1, 0, 42), False)

    def test_is_triangulo_retangulo_espera_true_quando_a2_igual_b2_mais_c2(
            self):
        self.assertEqual(self.triangulo.is_triangulo_retangulo(10, 8, 6), True)

    def test_is_triangulo_retangulo_espera_false_quando_a2_diferente_b2_mais_c2(
            self):
        self.assertEqual(self.triangulo.is_triangulo_retangulo(1, 1, 2), False)

    def test_is_triangulo_obtusangulo_espera_true_quando_a2_maior_b2_mais_c2(
            self):
        self.assertEqual(self.triangulo.is_triangulo_obtusangulo(10, 6, 6),
                         True)

    def test_is_triangulo_obtusangulo_espera_false_quando_a2_menor_b2_mais_c2(
            self):
        self.assertEqual(self.triangulo.is_triangulo_obtusangulo(10, 8, 6),
                         False)

    def test_is_triangulo_acutangulo_espera_true_quando_a2_menor_b2_mais_c2(
            self):
        self.assertEqual(self.triangulo.is_triangulo_acutangulo(6, 6, 6), True)

    def test_is_triangulo_acutangulo_espera_false_quando_a2_maior_b2_mais_c2(
            self):
        self.assertEqual(self.triangulo.is_triangulo_acutangulo(10, 6, 6),
                         False)

    def test_is_triangulo_equilatero_espera_true_quando_lados_sao_iguais(self):
        self.assertEqual(self.triangulo.is_triangulo_equilatero(6, 6, 6), True)

    def test_is_triangulo_equilatero_espera_false_quando_lados_sao_diferentes(
            self):
        self.assertEqual(self.triangulo.is_triangulo_equilatero(15, 6, 6),
                         False)


if __name__ == '__main__':
    unittest.main()
