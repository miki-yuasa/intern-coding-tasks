def main():
    from sys import stdin
    from multiprocessing import Pool   

    stdin = open('q2_in.txt')
    data = [list(map(int,line.rstrip().split())) for line in stdin.readlines()]
    print(data)


    #S_lengths, abc_counts = list_all_tribos(50)
    #print(count_abc([50,1002,3000], S_lengths, abc_counts))
    #print(list_all_tribos(50)) 

def count_abc(kpq, S_lengths, abc_counts):
    from multiprocessing import Pool   
    from functools import partial

    k,p,q = kpq
    abc_count = abc_counts[k - 1]

    pool = Pool(2)
    abc_subtrahends = pool.map(partial(sum_subtrahends, k = k, S_lengths = S_lengths, abc_counts = abc_counts),[(p,True),(q,False)])

    return abc_count - sum(abc_subtrahends) #abc_count   

def sum_subtrahends(pos_pq, k, S_lengths, abc_counts):
    import numpy as np

    pos_del:int = pos_pq[0] - 1 # First p_del letters won't be counted
    is_p:bool = pos_pq[1]
   
    if is_p:
        abc_subtrahend = p_subtrahends(pos_del, k, S_lengths, abc_counts)
    else:
        abc_subtrahend = q_subtrahends(pos_del, k, S_lengths, abc_counts)

    return abc_subtrahend

def p_subtrahends(pos_del, k, S_lengths, abc_counts):
    import numpy as np

    k_counter = k
    abc_subtrahend = np.zeros(3)

    # Find the depth of searching tree first
    for _ in range(k - 3):
        if k_counter <= 3:
            break

        elif pos_del <=  S_lengths[k_counter - 4]:
            k_counter -= 3

        elif  S_lengths[k_counter - 4] < pos_del or pos_del <=  sum(S_lengths[k_counter-4 : k_counter-3]):
            k_counter -= 2
            pos_del -= S_lengths[k_counter - 4]
            abc_subtrahend += abc_counts[k_counter - 4]

        else: #sum(S_lengths[k-4 : k-3]) <  p_del or p_del <=  S_lengths[k - 1]:
            k_counter -= 1
            pos_del -=  sum(S_lengths[k_counter-4 : k_counter-2])
            abc_subtrahend += sum(abc_counts[k_counter-4 : k_counter-2])

    abc_subtrahend += [1, 0, 0] if k_counter == 1 else [0, 1, 0] if k_counter == 2 else [0, 1, 0] if k_counter == 3 else 'Error'
    return abc_subtrahend

def q_subtrahends(pos_del, k, S_lengths, abc_counts):
    import numpy as np

    k_counter = k
    abc_subtrahend = np.zeros(3)

    # Find the depth of searching tree first
    for _ in range(k - 3):
        if k_counter <= 3:
            break

        elif pos_del <=  S_lengths[k_counter - 4]:
            k_counter -= 3
            pos_del -=  sum(S_lengths[k_counter-3 : k_counter-1])
            abc_subtrahend += sum(abc_counts[k_counter-3 : k_counter-1])

        elif  S_lengths[k_counter - 4] < pos_del or pos_del <=  sum(S_lengths[k_counter-4 : k_counter-3]):
            k_counter -= 2
            pos_del -= S_lengths[k_counter - 2]
            abc_subtrahend += abc_counts[k_counter - 2]

        else: #sum(S_lengths[k-4 : k-3]) <  p_del or p_del <=  S_lengths[k - 1]:
            k_counter -= 1

    abc_subtrahend += [1, 0, 0] if k_counter == 1 else [0, 1, 0] if k_counter == 2 else [0, 1, 0] if k_counter == 3 else 'Error'
    return abc_subtrahend

def list_all_tribos(k_max):
    """ 
    The lengths of a S_k term is a tribonacci nuber F_(k+1). Since the 
    maximum value of k is given (k = 50), each iteration of solution
    has less overhead for each loop by calculating all the possible
    S lengths first. Same for counts of a, b, and c for each S_k
    k >= 4
    """ 
    import numpy as np
    from multiprocessing import Pool

    S_abc_with_k_max = [    (1, 1, 1, k_max),
                            (1, 0, 0, k_max),
                            (0, 1, 0, k_max),
                            (0, 0, 1, k_max)    ]
    
    p = Pool(4)
    result = p.map(list_tribo, S_abc_with_k_max)

    return result[0], np.vstack(result[0:3]).T

def list_tribo(list_k_max):
    """
    list_k_max: 1 x 4 list to start the Tribonacci sequence and k_max such that
    [T1, T2, T3, k_max]
    """
    tribo_list, k_max = list(list_k_max[0:3]), list_k_max[3]

    for _ in range(3,k_max):
        tribo_list.append(sum(tribo_list[-3:]))

    return tribo_list

if __name__ == '__main__':
    main()