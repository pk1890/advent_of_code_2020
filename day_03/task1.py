from math import ceil
slope = (1,3)

f = open('input.txt')
lines = list(map(lambda x: x.replace('\n', ''), f.readlines()))

width = len(lines[0])
height = len(lines)

coords = list(map(lambda x: (x*slope[0], (x*slope[1])%width), range(int(ceil(height/slope[0])))))
print(len(list(
    filter(lambda x: x == '#',
        map(lambda x: lines[x[0]][x[1]],
            coords
        )
    )
)))