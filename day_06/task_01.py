
def get_unique_letters_count(group):
    return len(set(filter(lambda x: x != '\n', group)))

f = open('input.txt')
groups = f.read().split("\n\n")

print(sum(list(map(get_unique_letters_count, groups))))