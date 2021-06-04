import cProfile
from typing import List, Tuple

class SeatNeighbor:
    negative_distance: int
    left_seat: int
    right_seat: int

    def __init__(self,left_seat,right_seat):
        self.left_seat = left_seat
        self.right_seat = right_seat
        self.negative_distance = left_seat - right_seat

    def tuplify(self):
        return (self.negative_distance,[self.left_seat, self.right_seat])

def main():
    from os import cpu_count
    from sys import stdin
    from multiprocessing import Pool   
    from functools import partial

    with open('q3_in.txt') as stdin:
        data = [list(map(int,line.rstrip().split())) for line in stdin.readlines()]

    p:Pool = Pool(cpu_count())
    solutions:List[str] = p.map(sum_even_seats,data)

    with open("q3_out.txt", "w", encoding = "utf_8") as file:
        file.writelines(solutions)

def sum_even_seats(na_1: List[int]) -> str:
    import heapq
    import numpy as np
    import numpy.typing as npt

    n:int
    a_1:int
    n, a_1 = na_1

    #seat_neighbors: List[int] = [SeatNeighbor(1,a_1+1).tuplify(), SeatNeighbor(a_1,n+2).tuplify()]
    #heapq.heapify(seat_neighbors)

    seats: npt.ArrayLike = get_seats(n,a_1)

    seat_sum: int = 0

    for i in range(np.ceil(n/2).astype('int')-1):
        new_seat_ind: int = seats.argmax() + 1
        new_seats: npt.ArrayLike = get_seats(n, new_seat_ind)
        seats: npt.ArrayLike = np.minimum(seats, new_seats)

        #seat_num, seats = get_seated(na_1, seats)
        if i % 2 == 0:
            seat_sum += new_seat_ind

    empty_seats_inds: npt.ArrayLike = np.argwhere(seats==1) + 1

    if np.ceil(n/2)%2 == 0:
        seat_sum += np.sum(empty_seats_inds[1::2])
    else:
        seat_sum += np.sum(empty_seats_inds[::2])
    
    return '{:.0f}\n'.format(seat_sum)

def get_seats(n: int, a_i:int):
    import numpy as np
    import numpy.typing as npt

    added_seats: npt.ArrayLike = np.array([i for i in range(a_i-1, 0, -1)] + [i for i in range(n - (a_i - 1))])
    return added_seats

def get_seated(na_1:List[int], seat_neighbors:List[Tuple[int]]):
    import heapq
    import math

    farthest_seats = heapq.heappop(seat_neighbors)
    seat_ind:int = math.floor(sum(farthest_seats[1])/2)
    heapq.heappush(seat_neighbors,SeatNeighbor(farthest_seats[1][0], seat_ind).tuplify())
    heapq.heappush(seat_neighbors,SeatNeighbor(seat_ind, farthest_seats[1][1]).tuplify())

    return seat_ind, seat_neighbors

if __name__ == '__main__':
    main()