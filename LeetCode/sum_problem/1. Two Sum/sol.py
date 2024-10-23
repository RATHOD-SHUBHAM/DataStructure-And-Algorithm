class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        dic = {}

        for i in range(n):
            diff = target - nums[i]

            if diff in dic:
                return [i, dic[diff]]
            
            dic[nums[i]] = i