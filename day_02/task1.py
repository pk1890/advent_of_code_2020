def check_entry(line):
    tokens = line.split()
    password = tokens[2]
    char = tokens[1][0]
    minimum, maximum = tuple(map(lambda x: int(x), tokens[0].split("-")))
    counter = 0
    for c in password:
        if c == char:
            counter += 1
        if counter > maximum:
            return 0
    return 0 if counter < minimum else 1

f = open("input.txt")
print("Passwords good: ", sum(list(map(check_entry, f.readlines()))))
