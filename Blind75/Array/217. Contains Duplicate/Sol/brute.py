# TC: O(n^2) | Sc: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # For every element 
        for i in range(n):
            # Compare with every other element
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        
        return False