def main():
    S_lengths, abc_counts = list_all_tribonacci_nums(50)
    print(count_abc([50,1002,3000], S_lengths, abc_counts))

def count_abc(kpq, S_lengths, abc_counts):
    k,p,q = kpq
    
    p_del = p - 1 # First p_del letters won't be counted
    
    abc_count = abc_counts[k - 1]
    k_counter = k

    # Find the depth of searching tree first
    for i in range(k - 3):
        if k_counter <= 3:
            break
        elif p_del <=  S_lengths[k_counter - 4]:
            k_counter -= 3
        elif  S_lengths[k_counter - 4] < p_del or p_del <=  sum(S_lengths[k_counter-4 : k_counter-3]):
            k_counter -= 2
            abc_count -= abc_counts[k_counter - 4]
            p_del -= S_lengths[k_counter - 4]
        else: #sum(S_lengths[k-4 : k-3]) <  p_del or p_del <=  S_lengths[k - 1]:
            k_counter -= 1
            abc_count -= sum(abc_counts[k_counter-4 : k_counter-2])
            p_del -=  sum(S_lengths[k_counter-4 : k_counter-2])

    abc_count -= [1, 0, 0] if k_counter == 1 else [0, 1, 0] if k_counter == 2 else [0, 1, 0] if k_counter == 3 else 'Error'
           
    return abc_count       


def list_all_tribonacci_nums(k_max):
    """ 
    The lengths of a S_k term is a tribonacci nuber F_(k+1). Since the 
    maximum value of k is given (k = 50), each iteration of solution
    has less overhead for each loop by calculating all the possible
    S lengths first. Same for counts of a, b, and c for each S_k
    k >= 4
    """ 
    import numpy as np

    S_lengths = [1, 1, 1]
    a_counts = [1, 0, 0]
    b_counts = [0, 1, 0]
    c_counts = [0, 0, 1]

    for i in range(3,k_max):
        S_lengths.append(sum(S_lengths[-3:]))
        a_counts.append(sum(a_counts[-3:]))
        b_counts.append(sum(b_counts[-3:]))
        c_counts.append(sum(c_counts[-3:]))

    return np.array(S_lengths), np.vstack([a_counts, b_counts, c_counts]).T

if __name__ == '__main__':
    main()