def check_num(numbers, index):
    sum = numbers[index]
    for first_pos in range(-25, 0):
        other = sum - numbers[index+first_pos]
        for sec_pos in range(-25, 0):
            if sec_pos != first_pos and numbers[index+sec_pos] == other:
                return True
    return False


numbers = list(map(lambda x: int(x), open('input.txt').readlines()))

for i in range(25, len(numbers)):
    if not check_num(numbers, i):
        print("FIRST WRONG ON POSITION ", i, ": ", numbers[i])
        exit()