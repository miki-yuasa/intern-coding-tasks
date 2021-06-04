import cProfile
from typing import List, Tuple

class SeatPair:
    distance: int
    half_distance: int
    left_seat: int
    right_seat: int

    def __init__(self,left_seat,right_seat):
        import math
        self.left_seat = left_seat
        self.right_seat = right_seat
        self.distance = left_seat - right_seat
        self.half_distance = math.floor(self.distance/2)

    def tuplify(self):
        return (self.half_distance,[self.left_seat, self.right_seat], self.distance)

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
    import math
    import numpy as np
    import numpy.typing as npt

    n:int
    a_1:int
    n, a_1 = na_1

    seat_sum: int = 0


    seat_pairs: List[Tuple] = initialize_seat_heap(n,a_1)

    for i in range(n-1):
        farthest_seat_pair = heapq.heappop(seat_pairs)

        if farthest_seat_pair[1][1] == a_1:

        elif farthest_seat_pair[1][0] == a_1:

        else:
            new_seat_ind:int = math.floor(sum(farthest_seat_pair[1])/2)
            heapq.heappush(seat_pairs,SeatPair(farthest_seat_pair[1][0], new_seat_ind).tuplify())
            heapq.heappush(seat_pairs,SeatPair(new_seat_ind, farthest_seat_pair[1][1]).tuplify())
         
    """
    seat_neighbors: List[int]
    closer_seats: Tuple
    seat_sum: int

    if np.floor(n/2) >= a_1:
        seat_neighbors = [SeatPair(a_1,n).tuplify()]
        closer_seats = SeatPair(1,a_1).tuplify()
        seat_sum = n
    else:
        seat_neighbors = [SeatPair(1,a_1).tuplify()]
        closer_seats = SeatPair(a_1,n).tuplify()
        seat_sum = 1

    closer_dist: int = closer_seats[0] - 1

    heapq.heapify(seat_neighbors)

    restart_ind: int

    for i in range(n-2):
        farthest_seats = heapq.heappop(seat_neighbors)

        if farthest_seats[0] == closer_dist:
            heapq.heappush(seat_neighbors, closer_seats)
            heapq.heappush(seat_neighbors, farthest_seats)
            restart_ind = i + 1
            if i % 2 == 1:
                seat_sum += 1
            else:
                pass
            break
        else:
            pass

        new_seat_ind:int = math.floor(sum(farthest_seats[1])/2)
        heapq.heappush(seat_neighbors,SeatPair(farthest_seats[1][0], new_seat_ind).tuplify())
        heapq.heappush(seat_neighbors,SeatPair(new_seat_ind, farthest_seats[1][1]).tuplify())

        if i % 2 == 1:
            seat_sum += new_seat_ind
        else:
            pass

    for i in range(restart_ind, n - 2):
        farthest_seats = heapq.heappop(seat_neighbors)

        new_seat_ind:int = math.floor(sum(farthest_seats[1])/2)
        heapq.heappush(seat_neighbors,SeatPair(farthest_seats[1][0], new_seat_ind).tuplify())
        heapq.heappush(seat_neighbors,SeatPair(new_seat_ind, farthest_seats[1][1]).tuplify())

        if i % 2 == 1:
            seat_sum += new_seat_ind
        else:
            continue
    """
    
    return '{:.0f}\n'.format(seat_sum)

def initialize_seat_heap(n:int, a_1:int) -> List[Tuple]:
    import heapq
    
    seat_pairs: List[Tuple] = [SeatPair(2-a_1,a_1).tuplify(), SeatPair(a_1,2*n-a_1).tuplify()]
    heapq.heapify(seat_pairs)

    return seat_pairs


def get_seated(n:int, a_i:int, seat_neighbors:List[Tuple[int]]):
    import heapq
    import math

    farthest_seats = heapq.heappop(seat_neighbors)
    seat_ind:int = math.floor(sum(farthest_seats[1])/2)
    heapq.heappush(seat_neighbors,SeatPair(farthest_seats[1][0], seat_ind).tuplify())
    heapq.heappush(seat_neighbors,SeatPair(seat_ind, farthest_seats[1][1]).tuplify())

    return seat_ind, seat_neighbors

if __name__ == '__main__':
    main()