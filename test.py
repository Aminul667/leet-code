nums = [3,2,4]
target = 6

numsMap = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff not in numsMap:
        numsMap[nums[i]] = i
    else:
        print([numsMap[diff], i])