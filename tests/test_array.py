import unittest

from algorithms import array


class TestArray(unittest.TestCase):

    """ Initialize array. """
    def setUp(self):
        print('Runs setUp() method before the test.')
        self.array = array.Array(6, '1 2 3 4 10 11')
    
    """ Tests that the sum of all numbers. """
    def test_sum(self):
        result = self.array.naiveSum()
        self.assertEqual(result, 31)

    """ Tests that an exception occurs when the number of arguments is different."""
    def test_sum_raise_exception(self):
        self.assertRaises(Exception, array.Array(5, '1 2 3 4 10 11'))

    """ Test that the part sum of all numbers. """
    def test_psum(self):
        result = self.array.partSum(1, 4)
        self.assertEqual(result, 19)
        
    """ Print message. """
    def tearDown(self):
        print('Runs tearDown() method after the test.')

