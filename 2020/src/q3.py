from __future__ import annotations
import cProfile
from typing import List, Tuple
from functools import lru_cache

@lru_cache
def main():
    from os import cpu_count
    from sys import stdin
    from multiprocessing import Pool   
    from functools import partial

    with open('q3_in.txt') as stdin:
        data = [tuple(map(int,line.rstrip().split())) for line in stdin.readlines()]

    p:Pool = Pool(cpu_count())
    solutions:List[str] = p.map(sum_even_seats, data)

    with open("q3_out.txt", "w", encoding = "utf_8") as file:
        file.writelines(solutions)

@lru_cache
def sum_even_seats(na_1: Tuple[int]) -> str:
    from heapq import heappop, heapify, heappush

    n:int
    a_1:int
    n, a_1 = na_1

    seat_sum: int = 0
    seat_pairs: List[Tuple] = initialize_seat_heap(n,a_1)

    for i in range(n-1):
        farthest_seat_pair = heappop(seat_pairs)
        new_seat_ind:int

        left_seat: int = farthest_seat_pair[1][0]
        right_seat: int = farthest_seat_pair[1][1]

        if left_seat <= 0:
            new_seat_ind = 1
            heappush(seat_pairs, get_seat_pair(1, a_1))

        elif right_seat >= n + 1:
             new_seat_ind = n
             heappush(seat_pairs, get_seat_pair(a_1, n))

        else:
            new_seat_ind = left_seat - farthest_seat_pair[0]
            heappush(seat_pairs, get_seat_pair(left_seat, new_seat_ind))
            heappush(seat_pairs, get_seat_pair(new_seat_ind, right_seat))

        if i % 2 == 0:
            seat_sum += new_seat_ind
        else:
            pass
    
    return '{:.0f}\n'.format(seat_sum)

@lru_cache
def initialize_seat_heap(n:int, a_1:int) -> List[Tuple]:
    from heapq import heapify
    
    seat_pairs: List[Tuple] = [get_seat_pair(2-a_1,a_1), get_seat_pair(a_1,2*n-a_1)]
    heapify(seat_pairs)

    return seat_pairs

@lru_cache
def get_seat_pair(left_seat: int, right_seat: int) -> Tuple:
    from math import ceil 

    return (ceil((left_seat - right_seat)/2), [left_seat, right_seat], left_seat - right_seat)


if __name__ == '__main__':
    main()