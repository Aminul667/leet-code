class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if  diff in numsMap:
                return [numsMap[diff], i]
            numsMap[nums[i]] = i
        return []

# a = Solution()
# print(a.twoSum([3, 2, 4], 6))