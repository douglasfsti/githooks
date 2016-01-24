#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Triangulo(object):
    """
    Tipos de Triângulos
    ===================

    Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem
    decrescente, de modo que o lado A representa o maior dos 3 lados.
    A seguir, determine o tipo de triângulo que estes três lados formam, com
    base nos seguintes casos, sempre escrevendo uma mensagem adequada:
        se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
        se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
        se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
        se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
        se os três lados forem iguais, apresente a mensagem:
                                                           TRIANGULO EQUILATERO
        se apenas dois dos lados forem iguais, apresente a mensagem:
                                                           TRIANGULO ISOSCELES

    Entrada
    =======

    A entrada contem três valores de ponto flutuante de dupla precisão

    A (0 < A) , B (0 < B) e C (0 < C).

    Saída
    =====

    Imprima todas as classificações do triângulo especificado na entrada.
    """

    def valores_sao_maiores_que_zero(self, a, b, c):
        return a > 0 and b > 0 and c > 0

    def possui_apenas_dois_lados_iguais(self, a, b, c):
        return a == b or a == c or b == c

    def is_triangulo(self, a, b, c):
        return self.valores_sao_maiores_que_zero(a, b, c) and b + c >= a

    def is_triangulo_retangulo(self, a, b, c):
        return self.is_triangulo(a, b, c) and b ** 2 + c ** 2 == a ** 2

    def is_triangulo_obtusangulo(self, a, b, c):
        return self.is_triangulo(a, b, c) and a ** 2 > b ** 2 + c ** 2

    def is_triangulo_acutangulo(self, a, b, c):
        return self.is_triangulo(a, b, c) and a ** 2 < b ** 2 + c ** 2

    def is_triangulo_equilatero(self, a, b, c):
        return self.is_triangulo(a, b, c) and a == b == c

    def is_triangulo_isosceles(self, a, b, c):
        return (self.is_triangulo(a, b, c) and
                not self.is_triangulo_equilatero(a, b, c) and
                self.possui_apenas_dois_lados_iguais(a, b, c))
