# Test case for Question 2

import unittest
import numpy as np
import q2

class TestQ2(unittest.TestCase):
    #def test_count_abc_example(self):
    #    self.assertEqual([1,0,1],q2.count_abc([5,2,3]))
    
    def list_all_tribonacci_nums(self):
        self.assertEqual(q2.list_all_tribonacci_nums(4)[0],[1,1,1,3])
        self.assertEqual(q2.list_all_tribonacci_nums(5)[0],[1,1,1,3,5])
        self.assertEqual(50,len(q2.list_all_tribonacci_nums(50)[0]))
        self.assertEqual(True,np.allclose(q2.list_all_tribonacci_nums(5)[1],np.array([[1,0,0,1,1],[0,1,0,1,2],[0,0,1,1,2]])))

    def test_S_chars(self):
        self.assertEqual('a',q2.S_chars(1))
        self.assertEqual('b',q2.S_chars(2))
        self.assertEqual('c',q2.S_chars(3))
        self.assertEqual('abc',q2.S_chars(4))
        self.assertEqual('bcabc',q2.S_chars(5))


