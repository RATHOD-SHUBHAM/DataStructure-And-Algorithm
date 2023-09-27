# Tc: O(nlogn) | Sc: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Sort array
        nums.sort()
        
        for i in range(1, n):
            # Check if predecessor is same as current val
            if nums[i] == nums[i-1]:
                return True
        
        return False