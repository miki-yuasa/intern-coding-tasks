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
        return((self.negative_distance,[self.left_seat, self.right_seat]))

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

    n:int
    a_1:int
    n,a_1 = na_1[0]

    seat_neighbors: List[int] = [SeatNeighbor(0,a_1).tuplify(), SeatNeighbor(a_1,n).tuplify()]
    heapq.heapify(seat_neighbors)

    seat_sum: int = 0

    for i in range(n-1):
        seat_num, seat_neighbors = get_seated(na_1, seat_neighbors)
        if i % 2 == 1:
            seat_sum += seat_num

    return '{:.0f}\n'.format(seat_sum)

def get_seated(na_1:List[int], seat_neighbors:List[Tuple[int]]):
    import heapq
    import math

    farthest_seats = heapq.heappop(seat_neighbors)
    seat_ind:int = math.floor(sum(seat_neighbors[1])/2)
    heapq.heappush(seat_neighbors,SeatNeighbor(seat_neighbors[1][0], seat_ind).tuplify())
    heapq.heappush(seat_neighbors,SeatNeighbor(seat_ind, seat_neighbors[1][1]).tuplify())

    return seat_ind, seat_neighbors

if __name__ == '__main__':
    main()