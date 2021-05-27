import unittest
import code


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(code.add(1, 2), 3)

    def test_subtract_1(self):
        self.assertEqual(code.subtract(3, 2), 1)

    def test_times_1(self):
        self.assertEqual(code.times(2, 2), 4)

    def test_divide_1(self):
        self.assertEqual(code.div(2, 2), 1)


if __name__ == '__main__':
    unittest.main()
