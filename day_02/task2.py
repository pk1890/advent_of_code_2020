def check_entry(line):
    tokens = line.split()
    password = tokens[2]
    char = tokens[1][0]
    pos1, pos2 = tuple(map(lambda x: int(x), tokens[0].split("-")))
    return len(password) >= pos2 and ((password[pos1-1] == char) != (password[pos2-1] == char))
    

f = open("input.txt")
print("Passwords good: ", sum(list(map(check_entry, f.readlines()))))
