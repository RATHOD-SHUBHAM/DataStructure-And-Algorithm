# Tc and Sc : O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        dic = {}
        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        
        for key, value in dic.items():
            if value == 1:
                return key