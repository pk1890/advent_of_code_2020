import functools
from math import floor, ceil

def update_range(range, is_upper_half):
    min, max = range
    half = (min+max)/2
    if is_upper_half:
        return (ceil(half) ,max)
    else:
        return (min , floor(half))


def bisect(min, max, is_upper_half_char, values):
    return functools.reduce(update_range, map(lambda x: x == is_upper_half_char, values), (min, max))[0]

def get_seat_id(seat):
    row_info = seat[:7]
    column_info = seat[7:]
    
    row = bisect(0, 127, 'B', row_info)
    column = bisect(0, 7, 'R', column_info)

    return row*8 + column


f = open('input.txt')
seats = f.readlines()
seat_ids = list(map(get_seat_id, seats))
seat_ids.sort()

single_empty_seats = []

for i in range(0, len(seat_ids)-1):
    if seat_ids[i+1]-seat_ids[i] == 2:
        single_empty_seats.append(seat_ids[i]+1)

print("OCCUPIED: ", seat_ids)
print("SINGLE EMPTY: ", single_empty_seats)