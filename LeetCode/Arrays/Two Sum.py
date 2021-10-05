nums = [2,7,11,15]
target = 9
dict = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in dict:
        print([dict[diff],i])
    else:
        dict[nums[i]] = i