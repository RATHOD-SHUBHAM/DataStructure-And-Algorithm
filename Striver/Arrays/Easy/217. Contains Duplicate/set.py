# Tc: O(n) | Sc: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        unique_ele = set()

        for i in range(n):
            if nums[i] in unique_ele:
                return True
            
            unique_ele.add(nums[i])
        
        return False