# time complexity = o(n)
# space complexity = o(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        if len(nums) == 0 or len(nums) == 1:
            return []
        
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dic:
                return [dic[diff],i]
            else:
                dic[nums[i]] = i