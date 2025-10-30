# Tc and Sc = O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
# ------------------------Dictionary-----------------------------------

# Tc and Sc = O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            dic[nums[i]] = 1
            
        return False
    
# ----------------------------Set-------------------------------    

# Tc | Sc: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        storage = set()

        for val in nums:
            if val in storage:
                return True
            else:
                storage.add(val)
        
        return False