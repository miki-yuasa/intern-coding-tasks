# Test cases for Question 3

import unittest
import numpy as np
import q3
from itertools import combinations 

class TestQ3(unittest.TestCase):

    def test_get_seat(self):
        
        test_patterns = [
            (6,1,13),
            (6,2,12),
            (6,3,13),
            (6,4,8),
            (6,5,9),
            (6,6,8)
        ]

        for n, a_1, expected_result in test_patterns:
            with self.subTest(n=n, a_1=a_1):
                self.assertEqual('{:.0f}\n'.format(expected_result), q3.sum_even_seats([n,a_1]))

if __name__ == '__main__':
    unittest.main()