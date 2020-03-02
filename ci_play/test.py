import unittest

import my_functions

class TestMyFunc(unittest.TestCase):

    def setUp(self):
        pass

    def test_addTwoNumbers(self):
        self.assertEqual( my_functions.add_two_numbers(5,7), 12)

    def test_multiplyTwoNumbers(self):
        self.assertEqual( my_functions.multiply_two_numbers(5,5), 25)
        
    def test_addTwoNumbers_1(self):
        self.assertEqual( my_functions.add_two_numbers(5,12), 17)
        
    def test_multiplyTwoNumbers_1(self):
        self.assertEqual( my_functions.multiply_two_numbers(3,5), 15)

if __name__ == '__main__':
    unittest.main()
