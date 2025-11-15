import unittest
from math import sqrt
from vector.Vector import Vector   # предполагаем, что твой класс лежит в файле vector.py

class TestVector(unittest.TestCase):

    def test_init_get_set(self):
        v1 = Vector(1, 2, 3)
        self.assertEqual(v1.get(), [1, 2, 3])

        v2 = Vector(4, 5, 6)
        v1.set(v2)
        self.assertEqual(v1.get(), [4, 5, 6])

    def test_print_coords_no_error(self):
        v = Vector(1, 2, 3)
        # просто проверяем, что метод вызывается без исключений
        v.print_coords()

    def test_length(self):
        v = Vector(3, 4, 0)
        self.assertEqual(v.length(), 5.0)
        v = Vector(0, 0, 0)
        self.assertEqual(v.length(), 0.0)

    def test_add_and_iadd(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        v3 = v1 + v2
        self.assertEqual(v3.get(), [5, 7, 9])

        v4 = Vector(1, 1, 1)
        v4 += Vector(2, 2, 2)
        self.assertEqual(v4.get(), [3, 3, 3])

    def test_sub_and_isub(self):
        v1 = Vector(5, 7, 9)
        v2 = Vector(1, 2, 3)
        v3 = v1 - v2
        self.assertEqual(v3.get(), [4, 5, 6])

        v4 = Vector(10, 10, 10)
        v4 -= Vector(1, 2, 3)
        self.assertEqual(v4.get(), [9, 8, 7])

    def test_mul_vector_and_scalar(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        self.assertEqual(v1 * v2, 1*4 + 2*5 + 3*6)
        self.assertEqual(v1 * 2, 1*2 + 2*2 + 3*2)

    def test_truediv(self):
        v1 = Vector(10, 20, 30)
        v2 = Vector(2, 4, 5)
        v3 = v1 / v2
        self.assertEqual(v3.get(), [5.0, 5.0, 6.0])

    def test_xor_and_ixor(self):
        v1 = Vector(1, 0, 0)
        v2 = Vector(0, 1, 0)
        cos_angle = v1 ^ v2
        self.assertAlmostEqual(cos_angle, 0.0, places=5)

        cos_angle2 = v1 ^ v1
        self.assertAlmostEqual(cos_angle2, 1.0, places=5)

        cos_angle3 = v1 ^ v2
        cos_angle4 = v1 ^ v2
        self.assertEqual(cos_angle3, cos_angle4)

    def test_comparisons(self):
        v1 = Vector(3, 0, 0)  # length = 3
        v2 = Vector(4, 0, 0)  # length = 4
        v3 = Vector(3, 0, 0)  # length = 3

        self.assertTrue(v1 == v3)
        self.assertTrue(v1 != v2)
        self.assertTrue(v1 < v2)
        self.assertTrue(v1 <= v3)
        self.assertTrue(v2 > v1)
        self.assertTrue(v2 >= v3)

    def test_invalid_operations(self):
        v = Vector(1, 2, 3)

        # просто проверяем, что методы не падают при неправильных типах
        v + 5
        v - 5
        v * "abc"
        v / 5
        v == "abc"
        v < "abc"


if __name__ == "__main__":
    unittest.main()
