import unittest
import math
import sys
sys.path.append("..")  # Добавляем путь к модулю

from triangle import area, perimeter  # Импортируем функции из модуля triangle

class TriangleTestCase(unittest.TestCase):

    def test_zero_sides(self):
        """Тест для сторон треугольника равных 0"""
        a, b, c = 0, 0, 0
        with self.assertRaises(ValueError):
            area(a, b, c)

        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_positive_sides(self):
        """Тест для положительных сторон треугольника"""
        a, b, c = 3, 4, 5  # Прямоугольный треугольник
        expected_area = 6  # Площадь треугольника (по формуле Герона)
        expected_perimeter = 12

        self.assertAlmostEqual(area(a, b, c), expected_area)
        self.assertEqual(perimeter(a, b, c), expected_perimeter)

    def test_invalid_triangle_inequality(self):
        """Тест для сторон, не удовлетворяющих неравенству треугольника"""
        a, b, c = 1, 2, 10  # Неравенство треугольника нарушено
        with self.assertRaises(ValueError):
            area(a, b, c)

        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_negative_sides(self):
        """Тест для отрицательных сторон"""
        a, b, c = -3, 4, 5  # Отрицательная сторона
        with self.assertRaises(ValueError):
            area(a, b, c)

        with self.assertRaises(ValueError):
            perimeter(a, b, c)

if __name__ == '__main__':
    unittest.main()
