import unittest
import code


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(code.add(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
