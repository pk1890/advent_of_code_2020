f = open('input.txt')
nums = list(map(lambda x: int(x), f.readlines()))
nums.sort()
for i in range(0, len(nums)):
    if i < 2020:
        for j in range(len(nums)-1, i-1, -1):
            if nums[i] + nums[j] == 2020:
                print("FOUND!!!", nums[i], nums[j])
                print(nums[i]*nums[j])
                exit(0)
