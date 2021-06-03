# Test cases for Question 1

import unittest
import numpy as np
import q1
from itertools import combinations 

class TestQ1(unittest.TestCase):

    def test_count_matrices(self):
        row_combinations = list(combinations(range(8),3)) # 8C3 = 56 in total
        test_patterns = [
            (0,1,2,3),
            (0,1,99,0)
        ]

        for x, y, d, expected_result in test_patterns:
            with self.subTest(x=x, y=y, d=d):
                self.assertEqual('{:.0f}\n'.format(expected_result), q1.count_matrices([x,y,d],row_combinations))

if __name__ == '__main__':
    unittest.main()