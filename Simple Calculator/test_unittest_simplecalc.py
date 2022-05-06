from simple_calc import SimpleCalc
import unittest


class CalcTest(unittest.TestCase):
    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2,4),6)  # add assertion here

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6,4),2)


if __name__ == '__main__':
    unittest.main()
