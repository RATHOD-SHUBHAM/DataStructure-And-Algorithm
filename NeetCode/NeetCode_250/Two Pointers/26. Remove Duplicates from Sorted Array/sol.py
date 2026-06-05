# Idea is instead of swapping the unwated element copy the needed element in right index
# We anywasy dont care about element that is after k unique elements

# Tc: O(n) | SC: O(1)

"""
Two pointers where i is the writer (last valid position) and j is the reader (scout). 
When reader finds something new, writer steps forward and copies it. Works because sorted = duplicates are adjacent.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0 # last confirmed unique position

        for j in range(1, n):
            if nums[i] != nums[j]: # found a new unique element
                i += 1 # Move a step to identify duplicate
                nums[i] = nums[j] # place it right after last unique
            
        return i + 1
        