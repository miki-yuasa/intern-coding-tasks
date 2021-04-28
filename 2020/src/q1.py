def main():
    x = 0
    y = 1
    d = 2

    display_solution(x,y,d,count_matrices(x,y,d))

def count_matrices(x:int, y:int, d:int)->int:
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
    # potential matrices are always 8 * (8-1) = 56.

    if d == 0:
        return 56 # always 8 * (8-1) = 56 when d = 0.

    else:
        from itertools import combinations
        import numpy as np

        possible_rows = np.array([[ x, x, x ],
                                  [ x, x, y ],
                                  [ x, y, x ],
                                  [ y, x, x ],
                                  [ y, y, x ],
                                  [ y, x, y ],
                                  [ x, y, y ],
                                  [ y, y, y]])
        row_combinations = combinations(range(8),3)

        i = 0

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

if __name__ == '__main__':
    main()