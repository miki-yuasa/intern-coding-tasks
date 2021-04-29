# Test case for Question 2

import unittest
import numpy as np
import q2

class TestQ2(unittest.TestCase):
    #def test_count_abc_example(self):
    #    self.assertEqual([1,0,1],q2.count_abc([5,2,3]))
    """
    def test_list_all_S_lengths(self):
        self.assertEqual(True,np.allclose(q2.list_all_S_lengths(1),[1]))
        self.assertEqual(True,np.allclose(q2.list_all_S_lengths(2),[1]))
        self.assertEqual(True,np.allclose(q2.list_all_S_lengths(3),[1]))
        self.assertEqual(True,np.allclose(q2.list_all_S_lengths(5),[1,1,1,3,5]))
        self.assertEqual(True,np.allclose(q2.list_all_S_lengths(10),[1,1,1,3,5,8,13,21,34,55]))
    """

    def test_S_chars(self):
        self.assertEqual('a',q2.S_chars(1))
        self.assertEqual('b',q2.S_chars(2))
        self.assertEqual('c',q2.S_chars(3))
        self.assertEqual('abc',q2.S_chars(4))
        self.assertEqual('bcabc',q2.S_chars(5))


