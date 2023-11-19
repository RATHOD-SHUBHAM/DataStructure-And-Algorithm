# Tc and Sc: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)
        
        for i in range(n):
            a = nums[i]
            # a + b = c; b = c - a
            b = target - a
            
            if b in dic:
                return [dic[b] , i]
            
            dic[a] = i