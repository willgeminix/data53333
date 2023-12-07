import unittest
import max_num as m


class TestMax(unittest.TestCase):

    def setUp(self):
        self.num1 = 10
        self.num2 = 20

    def test_max(self):
        self.assertEqual(m.max_num(self.num1, self.num2), 20)
        self.assertEqual(m.max_num(self.num2, self.num1), 20)


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(TestMax('test_max'))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()