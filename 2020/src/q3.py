import cProfile
from typing import List, Tuple

class SeatNeighbor:
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

    seat_neighbors: List[int]
    closer_seats: Tuple
    seat_sum: int

    if np.floor(n/2) >= a_1:
        seat_neighbors = [SeatNeighbor(a_1,n).tuplify()]
        closer_seats = SeatNeighbor(1,a_1).tuplify()
        seat_sum = n
    else:
        seat_neighbors = [SeatNeighbor(1,a_1).tuplify()]
        closer_seats = SeatNeighbor(a_1,n).tuplify()
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
        heapq.heappush(seat_neighbors,SeatNeighbor(farthest_seats[1][0], new_seat_ind).tuplify())
        heapq.heappush(seat_neighbors,SeatNeighbor(new_seat_ind, farthest_seats[1][1]).tuplify())

        if i % 2 == 1:
            seat_sum += new_seat_ind
        else:
            pass

    for i in range(restart_ind, n - 2):
        farthest_seats = heapq.heappop(seat_neighbors)

        new_seat_ind:int = math.floor(sum(farthest_seats[1])/2)
        heapq.heappush(seat_neighbors,SeatNeighbor(farthest_seats[1][0], new_seat_ind).tuplify())
        heapq.heappush(seat_neighbors,SeatNeighbor(new_seat_ind, farthest_seats[1][1]).tuplify())

        if i % 2 == 1:
            seat_sum += new_seat_ind
        else:
            continue     
    """
    for i in range(np.ceil(n/2).astype('int')-1):
        new_seat_ind: int = seats.argmax() + 1
        new_seats: npt.ArrayLike = get_seats(n, new_seat_ind)
        seats: npt.ArrayLike = np.minimum(seats, new_seats)

        #seat_num, seats = get_seated(na_1, seats)
        

    empty_seats_inds: npt.ArrayLike = np.argwhere(seats==1) + 1

    if np.ceil(n/2)%2 == 0:
        seat_sum += np.sum(empty_seats_inds[1::2])
    else:
        seat_sum += np.sum(empty_seats_inds[::2])
    """
    
    return '{:.0f}\n'.format(seat_sum)

def initialize_seat_heap(n:int, a_i:int) -> List[Tuple]:


def get_seated(n:int, a_i:int, seat_neighbors:List[Tuple[int]]):
    import heapq
    import math

    farthest_seats = heapq.heappop(seat_neighbors)
    seat_ind:int = math.floor(sum(farthest_seats[1])/2)
    heapq.heappush(seat_neighbors,SeatNeighbor(farthest_seats[1][0], seat_ind).tuplify())
    heapq.heappush(seat_neighbors,SeatNeighbor(seat_ind, farthest_seats[1][1]).tuplify())

    return seat_ind, seat_neighbors

if __name__ == '__main__':
    main()