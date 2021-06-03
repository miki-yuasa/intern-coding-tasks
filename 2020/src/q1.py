from typing import List, Tuple

def main():
    from os import cpu_count
    from sys import stdin
    from multiprocessing import Pool   
    from functools import partial
    from itertools import combinations 
    
    with open('q1_in.txt') as stdin:
        data = [list(map(int,line.rstrip().split())) for line in stdin.readlines()]

    row_combinations = list(combinations(range(8),3)) # 8C3 = 56 in total

    p = Pool(cpu_count())

    solutions = p.map(partial(count_matrices, row_combinations = row_combinations),data)
    with open("q1_out.txt", "w", encoding = "utf_8") as file:
        file.writelines(solutions)

def count_matrices(xyd: List[int], row_combinations: List[List[int]])->str:
    """
    The basic strategy to tack;e this problem is to use the property
    det|(a,b,c)'| = a (b x c) = b (c x a) = c (a x b) where a, b, and c are
    row vectors (i.e. scalar triple products). 

    The equation above infers that:
      1.  if two of the row vectors are switched, the determinant has an
          opposite sign. e.g. det|(a,b,c)'| = -det|(a,c,b)'|
      2.  if two rows are the same, the determinant is 0. 
          e.g. det|(a,b,b)'| = 0.

    Since the give matrix is always 3 by 3 and the elements are either x
    or y, the possible combination of elements in a row is 2^3 = 8. For case 1
    above, there are 8C3 = 56 combinations to examine. For case 2, the
    potential matrices are at least 8C2 *3 + 8 = 92.
    """

    import numpy as np

    x, y, d = xyd

    i = 92 if d == 0 else 0 # Count matching matrices

    possible_rows = np.array([[ x, x, x ],
                                [ x, x, y ],
                                [ x, y, x ],
                                [ y, x, x ],
                                [ y, y, x ],
                                [ y, x, y ],
                                [ x, y, y ],
                                [ y, y, y]])
    
    for combination in row_combinations:
        i += 1 if np.isclose(abs(d), abs(np.linalg.det(possible_rows[combination,:]))) \
             else 0
    
    """
    There are 3 possible combination of the rows based on the property
    of scalar triple products, so multiply by 3. 
    """
    return '{:.0f}\n'.format(i*3) 

if __name__ == '__main__':
    main()