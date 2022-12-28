import unittest
import main

# test sum function from main.py
class TestMain(unittest.TestCase):
    def test_sum(self):
        sum_param = 20
        result = main.sum(sum_param)
        self.assertEqual(result, 30)

if __name__ == '__main__':
# .main() just runs the test, it is not related to the file name
    unittest.main()