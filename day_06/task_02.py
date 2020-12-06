import functools

def get_everyone_letters_count(group):
    people = group.split('\n')
    return len(functools.reduce(lambda x, y: x & y, map(lambda x: set(x), people)))

f = open('input.txt')
groups = f.read().split("\n\n")

print(sum(list(map(get_everyone_letters_count, groups))))