# def count_arrangements(data):
#     if len(data) == 1:
#         return 1
#     joltage = data[0] 
#     end = -1
#     for i in range(1, len(data)): 
#         if data[i] - joltage <= 3:
#             end = i
#         else:
#             break
#     if end == -1: 
#         return 0
#     # print(data[1:end+1], data, end)
#     return sum([count_arrangements(data[start:]) for start in range(1, end+1)])



# nums = [0] + list(map(lambda x: int(x), open('input.txt').readlines()))
# nums.sort()
# nums.append(nums[-1]+3)
# print(nums)

# print(count_arrangements(nums))

nums = [0] + list(map(lambda x: int(x), open('input.txt').readlines()))
nums.sort()
nums.append(nums[-1]+3)

arrangements_to_i = [0] * len(nums)
arrangements_to_i[0] = 1

for i in range(len(nums)):
    for j in range(-i, 0):
        if nums[i] - nums[i+j] <=3:
            arrangements_to_i[i] += arrangements_to_i[i+j]
print(arrangements_to_i)
