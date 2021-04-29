import numpy as np

def main():
    #S_lengths = list_all_S_lengths(50)
    #print(S_lengths)
    S_chars(37)

def count_abc(inputs,S_lengths):
    return 0
    
"""
def list_all_S_lengths(k_max):
    """ """
    The lengths of a S_k term is a Fibonacci nuber F_(k+1). Since the 
    maximum value of k is give (k = 50), each iteration of solution
    has less overhead for each loop by calculating all the possible
    S lengths first. 
    A Fibonacci number can be computed by rounding based on Binet's
    formula approximated by the golden ratio phi = (1 + sqrt(5)) / 2:
    F_n = floor(phi^n/sqrt(5) + 1/2) when n > 0.
    """ """
        k = np.arange(4,k_max+1)
        return np.hstack([1, 1, 1, np.floor(1/np.sqrt(5)*((1+np.sqrt(5))/2)**k + 0.5)])
"""

def rec(S3, S2, S1, k):
    if k <= 3: 
        return S1
    else:    
        return rec(S2, S1, S3 + S2 + S1, k - 1)

def S_chars(k):
    return ['a', 'b', 'c'][k-1] if k <= 3 else rec('a', 'b', 'c', k)

if __name__ == '__main__':
    main()