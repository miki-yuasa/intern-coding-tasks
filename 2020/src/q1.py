def count_matrices(x:int ,y:int ,d:int)->int:
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

    import itertools

    if d == 0:
        return 56 # always 8 * (8-1) = 56
    

print(count_matrices(1,2,0))