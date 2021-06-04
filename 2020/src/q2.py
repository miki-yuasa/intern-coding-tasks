from __future__ import annotations
import cProfile
from typing import List, Tuple
from os import cpu_count
from sys import stdin
from multiprocessing import Pool
from functools import partial
import numpy as np


def main():

    with open('q2_in.txt') as stdin:
        data = [list(map(int, line.rstrip().split()))
                for line in stdin.readlines()]

    S_lengths: List[int]
    abc_counts: List[List[int]]
    S_lengths, abc_counts = list_all_tribos(50)

    p: Pool = Pool(cpu_count())
    solutions: List[str] = p.map(
        partial(count_abc, S_lengths=S_lengths, abc_counts=abc_counts), data)

    with open("q2_out.txt", "w", encoding="utf_8") as file:
        file.writelines(solutions)


def count_abc(kpq: List[int], S_lengths: List[int], abc_counts: List[List[int]]) -> str:

    k, p, q = kpq
    abc_count = abc_counts[k - 1]

    abc = (abc_count - p_subtrahends(p, k, S_lengths, abc_counts) -
           q_subtrahends(q, k, S_lengths, abc_counts)).tolist()

    return 'a:{:.0f},b:{:.0f},c:{:.0f}\n'.format(*abc)


def p_subtrahends(p: int, k: int, S_lengths: List[int], abc_counts: List[List[int]]) -> List[int]:

    abc_subtrahend: np.ndarray = np.zeros(3)

    if p == 1:
        return abc_subtrahend
    else:
        k_counter = k
        for _ in range(k - 2):
            if k_counter <= 3:
                break

            elif p <= S_lengths[k_counter - 4]:
                k_counter -= 3

            elif S_lengths[k_counter - 4] < p and p <= sum(S_lengths[k_counter-4: k_counter-2]):
                p -= S_lengths[k_counter - 4]
                abc_subtrahend += abc_counts[k_counter - 4]
                k_counter -= 2

            else:
                p -= sum(S_lengths[k_counter-4: k_counter-2])
                abc_subtrahend += sum(abc_counts[k_counter-4: k_counter-2])
                k_counter -= 1

        return abc_subtrahend


def q_subtrahends(q: int, k: int, S_lengths: List[int], abc_counts: List[List[int]]) -> List[int]:

    abc_subtrahend = np.zeros(3)

    if q == S_lengths[k - 1]:
        return abc_subtrahend
    else:
        k_counter = k
        for _ in range(k - 3):
            if k_counter <= 3:
                break

            elif q <= S_lengths[k_counter - 4]:
                abc_subtrahend += sum(abc_counts[k_counter-3: k_counter-1])
                k_counter -= 3

            elif S_lengths[k_counter - 4] < q and q <= sum(S_lengths[k_counter-4: k_counter-2]):
                q -= S_lengths[k_counter - 4]
                abc_subtrahend += abc_counts[k_counter - 2]
                k_counter -= 2

            else:
                q -= sum(S_lengths[k_counter-4: k_counter-2])
                k_counter -= 1

        return abc_subtrahend


def list_all_tribos(k_max: int) -> Tuple[List[int], List[List[int]]]:
    """ 
    The lengths of a S_k term is a tribonacci nuber F_(k+1). Since the 
    maximum value of k is given (k = 50), each iteration of solution
    has less overhead for each loop by calculating all the possible
    S lengths first. Same for counts of a, b, and c for each S_k
    k >= 4
    """

    S_abc_with_k_max: List[List[int]] = [(1, 1, 1, k_max),
                                         (1, 0, 0, k_max),
                                         (0, 1, 0, k_max),
                                         (0, 0, 1, k_max)]

    p: Pool = Pool(4)
    result: List[List[int]] = p.map(list_tribo, S_abc_with_k_max)

    return result[0], np.vstack(result[1:4]).T


def list_tribo(list_k_max: List[int]) -> List[int]:
    """
    list_k_max: 1 x 4 list to start the Tribonacci sequence and k_max such that
    [T1, T2, T3, k_max]
    """
    k_max: int = list_k_max[3]
    tribo_list: List[int] = list(list_k_max[0:3]) + [0]*(k_max - 3)

    for i in range(3, k_max):
        tribo_list[i] = sum(tribo_list[i-3:i])

    return tribo_list


if __name__ == '__main__':
    main()
