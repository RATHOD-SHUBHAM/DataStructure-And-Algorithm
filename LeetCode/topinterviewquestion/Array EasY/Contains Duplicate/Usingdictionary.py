# Using Dictionary
# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return 
        
        
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            dic[nums[i]] = i
            
        return False