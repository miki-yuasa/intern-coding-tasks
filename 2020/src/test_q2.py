# Test case for Question 2

import unittest
import numpy as np
import q2

class TestQ2(unittest.TestCase):
    #def test_count_abc_example(self):
    #    self.assertEqual([1,0,1],q2.count_abc([5,2,3]))
    
    def list_all_tribonacci_nums(self):
        self.assertEqual(q2.list_all_tribos(4)[0],[1,1,1,3])
        self.assertEqual(q2.list_all_tribos(5)[0],[1,1,1,3,5])
        self.assertEqual(50,len(q2.list_all_tribos(50)[0]))
        self.assertEqual(True,np.allclose(q2.list_all_tribos(5)[1],np.array([[1,0,0,1,1],[0,1,0,1,2],[0,0,1,1,2]])))

    def test_count_abc(self):
        S_lengths, abc_counts = q2.list_all_tribos(50)
        self.assertEqual(True,np.allclose([1,0,1],q2.count_abc([5,2,3], S_lengths, abc_counts)))

