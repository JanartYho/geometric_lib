import unittest
import math
import sys
sys.path.append("..")  # Добавление пути к модулю

from circle import area, perimeter  # Импортируем функции из модуля circle

class CircleTestCase(unittest.TestCase):

    def test_zero_radius(self):
        """Тест для радиуса 0"""
        radius = 0
        expected_area = 0
        expected_perimeter = 0

        self.assertEqual(area(radius), expected_area)
        self.assertEqual(perimeter(radius), expected_perimeter)

    def test_positive_radius(self):
        """Тест для положительного радиуса"""
        radius = 1
        expected_area = math.pi
        expected_perimeter = 2 * math.pi

        self.assertEqual(area(radius), expected_area)
        self.assertEqual(perimeter(radius), expected_perimeter)

    def test_negative_radius(self):
        """Тест для отрицательного радиуса"""
        radius = -1

        with self.assertRaises(ValueError):
            area(radius)

        with self.assertRaises(ValueError):
            perimeter(radius)

    def test_non_numeric_radius(self):
        """Тест для некорректного типа радиуса"""
        radius = "string"

        with self.assertRaises(TypeError):
            area(radius)

        with self.assertRaises(TypeError):
            perimeter(radius)

if __name__ == '__main__':
    unittest.main()
