import unittest
import main

# test sum function from main.py
class TestMain(unittest.TestCase):
    def test_sum(self):
        sum_param = 20
        result = main.sum(sum_param)
        self.assertEqual(result, 30)

unittest.main()