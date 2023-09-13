import unittest
from library import Figure

class TestAddNumbers(unittest.TestCase):
    def test_circle_square(self):
        f = Figure(5.0)
        self.assertEqual(f.square(), 78.54)
    def test_right_triangle(self):
        self.assertEqual(Figure(3, 4, 5).square(), 6)
    def test_triangle(self):
        self.assertEqual(Figure(14, 13, 15).square(), 84)
        self.assertEqual(Figure(11, 9, 13).square(), 48.81)
    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            f = Figure(2.0, 3.0)
    def test_zero_sides(self):
        with self.assertRaises(ValueError):
            f = Figure(0.0, 0.0, 0.0)
    def test_negative_value(self):
        with self.assertRaises(ValueError):
            f = Figure(-5.0)
    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            f = Figure('3', '4', '6')
            f2 = Figure([1, 3, '2'])
            f3 = Figure({1:2})
    def test_valid_arguments(self):
        f1 = Figure(5)
        self.assertIsInstance(f1, Figure)
        
        f2 = Figure(42)
        self.assertIsInstance(f2, Figure)
    
if __name__ == '__main__':
    unittest.main()
