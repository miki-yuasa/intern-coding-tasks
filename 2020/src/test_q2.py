# Test case for Question 2

import unittest
import numpy as np
import q2

class TestQ2(unittest.TestCase):

    def list_all_tribonacci_nums(self):
        self.assertEqual(q2.list_all_tribos(4)[0],[1,1,1,3])
        self.assertEqual(q2.list_all_tribos(5)[0],[1,1,1,3,5])
        self.assertEqual(50,len(q2.list_all_tribos(50)[0]))
        self.assertEqual(True,np.allclose(q2.list_all_tribos(5)[1],np.array([[1,0,0,1,1],[0,1,0,1,2],[0,0,1,1,2]])))

    def test_count_abc(self):
        S_lengths, abc_counts = q2.list_all_tribos(50)
        
        self.assertEqual('a:{:.0f},b:{:.0f},c:{:.0f}\n'.format(*[1,0,1]), q2.count_abc([5,2,3], S_lengths, abc_counts))

    def test_subtrahends(self):
        test_patterns = [
            (1,5,[1,1,2]),
            (2,5,[1,1,1]),
            (3,5,[0,1,1]),
            (1,6,[2,3,3]),
            (2,6,[1,3,3]),
            (3,6,[1,2,3]),            
            (4,6,[1,2,2]),
            (5,6,[1,1,2]),
            (6,6,[1,1,1]),
        ]
        S_lengths, abc_counts = q2.list_all_tribos(50)

        for q, k, expected_result in test_patterns:
            with self.subTest(q=q, k=k):
                print(q,k,q2.q_subtrahends(q, k, S_lengths, abc_counts))
                self.assertEqual(True,np.allclose(q2.q_subtrahends(q, k, S_lengths, abc_counts),expected_result))
if __name__ == '__main__':
    unittest.main()