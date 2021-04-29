import numpy as np

def main():
    S_lengths = list_all_S_lengths(50)
    print(S_lengths)
    print(len(S_lengths))
    #S_chars(37)

def count_abc(inputs,S_lengths):
    return 0
    

def list_all_S_lengths(k_max):
    """ 
    The lengths of a S_k term is a tribonacci nuber F_(k+1). Since the 
    maximum value of k is given (k = 50), each iteration of solution
    has less overhead for each loop by calculating all the possible
    S lengths first. 
    """ 
    S_lengths = [1, 1, 1]
    
    for i in range(3,k_max):
        S_lengths.append(S_lengths[i-1] + S_lengths[i-2] + S_lengths[i-3])

    return S_lengths

def rec(S3, S2, S1, k):
    if k <= 3: 
        return S1
    else:    
        return rec(S2, S1, S3 + S2 + S1, k - 1)

def S_chars(k):
    return ['a', 'b', 'c'][k-1] if k <= 3 else rec('a', 'b', 'c', k)

if __name__ == '__main__':
    main()