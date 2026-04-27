import unittest
from main import calcular


class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calcular(2, 3, "+"), 5)

    def test_subtracao(self):
        self.assertEqual(calcular(5, 2, "-"), 3)

    def test_multiplicacao(self):
        self.assertEqual(calcular(4, 3, "*"), 12)

    def test_divisao(self):
        self.assertEqual(calcular(10, 2, "/"), 5)

    def test_divisao_por_zero(self):
        self.assertEqual(calcular(10, 0, "/"), "Erro: divisão por zero")


if __name__ == "__main__":
    unittest.main()