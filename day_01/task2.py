f = open('input.txt')
nums = list(map(lambda x: int(x), f.readlines()))
nums.sort()
for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        for k in range(len(nums)-1, j-1, -1):
            if nums[i] + nums[j] +nums[k]== 2020:
                print("FOUND!!!", nums[i], nums[j], nums[k])
                print(nums[i]*nums[j]*nums[k])
                exit(0)
