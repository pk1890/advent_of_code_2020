nums = [0] + list(map(lambda x: int(x), open('input.txt').readlines()))
nums.sort()
nums.append(nums[-1]+3)

diff_1, diff_3 = 0, 0
for i in range(1, len(nums)):
    diff = nums[i] - nums[i-1]
    if diff == 1:
        diff_1 += 1
    if diff == 3:
        diff_3 += 1

print(diff_1, diff_3, diff_1*diff_3)
