def check_num(numbers, index):
    sum = numbers[index]
    for first_pos in range(-25, 0):
        other = sum - numbers[index+first_pos]
        for sec_pos in range(-25, 0):
            if sec_pos != first_pos and numbers[index+sec_pos] == other:
                return True
    return False

numbers = list(map(lambda x: int(x), open('input.txt').readlines()))

first_wrong, wrong_index = 0, 0

for i in range(25, len(numbers)):
    if not check_num(numbers, i):
        print("FIRST WRONG ON POSITION ", i, ": ", numbers[i])
        first_wrong = numbers[i]
        wrong_index = i
        break

start, stop, curr_sum = 0, 0, 0
while stop < len(numbers):
    while curr_sum < first_wrong:
        curr_sum += numbers[stop]
        stop += 1
    
    if curr_sum == first_wrong:
        break

    while curr_sum > first_wrong:
        curr_sum -= numbers[start]
        start += 1
    
    if curr_sum == first_wrong:
        break

found_slice = numbers[start:stop]
print("ANSWER ", min(found_slice) + max(found_slice))