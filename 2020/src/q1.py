def main():
    from itertools import combinations
    from functools import partial
    import numpy as np
    
    data = read_file()
    row_combinations = list(combinations(range(8),3)) # 8C3 = 56 in total
    solution  = np.fromiter(map(partial(count_matrices, row_combinations = row_combinations), data), dtype=int).reshape((data.shape[0], 1))
    
    np.savetxt('q1_out.txt', np.hstack([data, solution]), fmt = '%.f', header = 'x y d solution' ) 

    #print(count_matrices([-3,-4,-4]))

def count_matrices(xyd, row_combinations)->int:
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
                                [ y, y, y]], dtype = int)
    
    for combination in row_combinations:
        i += 1 if np.isclose(np.abs(d), np.abs(np.linalg.det(possible_rows[combination,:]))) \
             else 0
    
    """
    There are 3 possible combination of the rows based on the property
    of scalar triple products, so multiply by 3. 
    """
    return i*3 

def display_solution(x:int, y:int, d:int, solution:int):
    print('Input:(', x, ',', y, ',', d, '), Output:', solution, sep='')

def read_file():
    import os
    import numpy as np

    file =  os.getcwd() + '/q1_in.txt'
    return np.loadtxt(file)

if __name__ == '__main__':
    main()