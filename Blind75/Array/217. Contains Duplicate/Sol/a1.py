# Brute Force

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
    
# ------------------------------------------------------------------
# Sort Technique

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

# ------------------------------------------------------------------   
# Hashmap/set

# Tc: O(n) | Sc: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        
        s_len = len(set_nums)
        
        n_len = len(nums)
        
        if n_len == s_len:
            return False
        else:
            return True