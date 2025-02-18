from __future__ import annotations
import cProfile
from typing import List, Tuple
from functools import lru_cache
from heapq import heapify, heappush, heapreplace
from os import cpu_count
from sys import stdin
from multiprocessing import Pool
from math import ceil
import numpy as np


@lru_cache
def main():
    with open('q3_in.txt') as stdin:
        data = [tuple(map(int, line.rstrip().split()))
                for line in stdin.readlines()]

    p: Pool = Pool(cpu_count())
    solutions: List[str] = p.map(sum_even_seats, data)

    with open("q3_out.txt", "w", encoding="utf_8") as file:
        file.writelines(solutions)


@lru_cache
def sum_even_seats(na_1: Tuple[int]) -> str:

    n: int
    a_1: int
    n, a_1 = na_1

    seat_pairs: List[Tuple] = initialize_seat_heap(n, a_1)

    sitting_order: List[int] = [a_1]

    ceiled_n_seats:int = ceil(n/2)

    for i in range(ceiled_n_seats - 1):
        farthest_seat_pair = seat_pairs[0]
        left_seat: int = farthest_seat_pair[1][0]
        right_seat: int = farthest_seat_pair[1][1]

        if left_seat <= 0:
            sitting_order.append(1)
            heapreplace(seat_pairs, get_seat_pair(1, a_1))

        elif right_seat >= n + 1:
            sitting_order.append(n)
            heapreplace(seat_pairs, get_seat_pair(a_1, n))

        else:
            new_seat_ind: int = left_seat - farthest_seat_pair[0]
            sitting_order.append(new_seat_ind)
            heapreplace(seat_pairs, get_seat_pair(left_seat, new_seat_ind))
            heappush(seat_pairs, get_seat_pair(new_seat_ind, right_seat))

    sat_seats = np.array(sitting_order)
    empty_seats = np.setdiff1d(np.array(range(1, n + 1)), sat_seats)

    empty_seats_count:int = np.sum(empty_seats[1::2]) if ceiled_n_seats % 2 == 0 else np.sum(empty_seats[0::2])

    print('Done',na_1)

    return '{:.0f}\n'.format(np.sum(sat_seats[1::2]) + empty_seats_count)


@lru_cache
def initialize_seat_heap(n: int, a_1: int) -> List[Tuple]:

    seat_pairs: List[Tuple] = [get_seat_pair(
        2-a_1, a_1), get_seat_pair(a_1, 2*n-a_1)]
    heapify(seat_pairs)

    return seat_pairs


@lru_cache
def get_seat_pair(left_seat: int, right_seat: int) -> Tuple:

    return (-((right_seat - left_seat)//2), [left_seat, right_seat])


if __name__ == '__main__':
    main()
