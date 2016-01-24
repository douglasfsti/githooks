import unittest

from triangulo.Triangulo import Triangulo
from triangulo.TrianguloEnums import TrianguloEnum


class TrianguloTestCases(unittest.TestCase):

    def setUp(self):
        self.triangulo = Triangulo()

    def tearDown(self):
        self.triangulo = None

    def test_is_triangulo_espera_true_quando_lados_sao_validos(self):
        self.assertEqual(self.triangulo.is_triangulo(10, 8, 6), True)

    def test_is_triangulo_espera_false_quando_lados_sao_invalidos(self):
        self.assertEqual(self.triangulo.is_triangulo(7, 5, 2), False)

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

    def test_is_triangulo_isosceles_espera_true_quando_dois_lados_sao_iguas(
            self):
        self.assertEqual(self.triangulo.is_triangulo_isosceles(10, 6, 6), True)

    def test_is_triangulo_isosceles_espera_falsse_quando_todos_lados_sao_iguais(
            self):
        self.assertEqual(self.triangulo.is_triangulo_isosceles(6, 6, 6),
                         False)

    def test_determinar_tipo_espera_nao_forma_triangulo_quando_valores_sao_invalidos(self):
        self.assertEqual(self.triangulo.determinar_tipo(5, 7, 2),
                         [TrianguloEnum.NAO_FORMA_TRIANGULO])

    def test_determinar_tipo_espera_triangulo_acutangulo_e_isosceles(self):
        self.assertEqual(self.triangulo.determinar_tipo(7, 5, 7),
                         [TrianguloEnum.TRIANGULO_ACUTANGULO,
                          TrianguloEnum.TRIANGULO_ISOSCELES])

    def test_determinar_tipo_espera_triangulo_obtusangulo_e_isosceles(self):
        self.assertEqual(self.triangulo.determinar_tipo(6, 6, 10),
                         [TrianguloEnum.TRIANGULO_OBTUSANGULO,
                          TrianguloEnum.TRIANGULO_ISOSCELES])

    def test_determinar_tipo_espera_triangulo_acutangulo_e_equilatero(self):
        self.assertEqual(self.triangulo.determinar_tipo(6, 6, 6),
                         [TrianguloEnum.TRIANGULO_ACUTANGULO,
                          TrianguloEnum.TRIANGULO_EQUILATERO])

    def test_determinar_tipo_espera_triangulo_retangulo(self):
        self.assertEqual(self.triangulo.determinar_tipo(6, 8, 10),
                         [TrianguloEnum.TRIANGULO_RETANGULO])


if __name__ == '__main__':
    unittest.main()
