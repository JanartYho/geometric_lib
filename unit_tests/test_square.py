import unittest
import sys
sys.path.append("..")  # Добавляем путь к модулю

from square import area, perimeter  # Импортируем функции из модуля square

class SquareTestCase(unittest.TestCase):

    def test_zero_side(self):
        """Тест для стороны квадрата равной 0"""
        side = 0
        expected_area = 0
        expected_perimeter = 0

        self.assertEqual(area(side), expected_area)
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_positive_side(self):
        """Тест для положительной стороны квадрата"""
        side = 1
        expected_area = 1
        expected_perimeter = 4

        self.assertEqual(area(side), expected_area)
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_negative_side(self):
        """Тест для отрицательной стороны квадрата"""
        side = -1

        with self.assertRaises(TypeError):
            area(side)

        with self.assertRaises(TypeError):
            perimeter(side)

if __name__ == '__main__':
    unittest.main()
