from math import ceil
import functools
import operator

def check_slope(slope):
    f = open('input.txt')
    lines = list(map(lambda x: x.replace('\n', ''), f.readlines()))
    f.close()
    width = len(lines[0])
    height = len(lines)

    coords = list(map(lambda x: (x*slope[0], (x*slope[1])%width), range(int(ceil(height/slope[0])))))
    return len(list(
        filter(lambda x: x == '#',
            map(lambda x: lines[x[0]][x[1]],
                coords
            )
        )
    ))

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

print(functools.reduce(operator.mul, map(check_slope, slopes), 1))