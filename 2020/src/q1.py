from itertools import combinations
import numpy as np
import os


def main():
    data = read_file()

    #solution = map(count_matrices,data)
    solution  = np.fromiter(map(count_matrices, data), dtype=np.int64).reshape((data.shape[0], 1))
    output = np.hstack([data, solution])
    np.savetxt('q1_out.txt', output, fmt = '%.f', header = 'x y d solution' ) 


def count_matrices(inputs)->int:
    # The basic strategy to tack;e this problem is to use the property
    # det|(a,b,c)'| = a (b x c) = b (c x a) = c (a x b) where a, b, and c are
    # row vectors (i.e. scalar triple products). 
    #
    # The equation above infers that:
    #   1.  if two of the row vectors are switched, the determinant has an
    #       opposite sign. e.g. det|(a,b,c)'| = -det|(a,c,b)'|
    #   2.  if two rows are the same, the determinant is 0. 
    #       e.g. det|(a,b,b)'| = 0.
    #
    # Since the give matrix is always 3 by 3 and the elements are either x
    # or y, the possible combination of elements in a row is 2^3 = 8. For case 1
    # above, there are 8C3 = 56 combinations to examine. For case 2, the
    # potential matrices are at least 8 * (8-1) *3 + 8 = 176.

    x = inputs[0]
    y = inputs[1]
    d = inputs[2]

    if d == 0:
        i = 176 # at least (8 * (8-1)) * 3 + 8 = 176 when d = 0.

    else:
        i = 0

    possible_rows = np.array([[ x, x, x ],
                                [ x, x, y ],
                                [ x, y, x ],
                                [ y, x, x ],
                                [ y, y, x ],
                                [ y, x, y ],
                                [ x, y, y ],
                                [ y, y, y]])
    row_combinations = combinations(range(8),3) # 8C3 = 56 in total

    for combination in row_combinations:
        a = possible_rows[combination[0]]
        b = possible_rows[combination[1]]
        c = possible_rows[combination[2]]

        if d == np.linalg.det([a,b,c]):
            i += 1
        elif d == np.linalg.det([a,c,b]):
            i += 1
        else:
            i += 0

    # There are 3 possible combination of the rows based on the property
    # of scalar triple products, so multiply by 3. 
    return i*3 

def display_solution(x:int, y:int, d:int, solution:int):
    print('Input:(', x, ',', y, ',', d, '), Output:', solution, sep='')

def read_file():
    file =  os.getcwd() + '/q1_in.txt'
    return np.loadtxt(file)

if __name__ == '__main__':
    main()