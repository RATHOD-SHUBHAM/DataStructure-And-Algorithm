# Tc and Sc: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}
        
        for i in range(n):
            diff = target - nums[i]
            
            if diff in dic:
                return [dic[diff], i]
            
            dic[nums[i]] = i