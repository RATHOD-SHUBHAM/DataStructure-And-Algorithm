"""
Difference with sorting and shifting:

The Issue
Classic insertion sort works by shifting elements right (one assignment), not swapping them (three assignments). 
Your version does extra work per iteration.

Your approach (swap-based):
nums[j], nums[j+1] = nums[j+1], nums[j]  # 3 operations per step

Classic approach (shift-based):
nums[j+1] = nums[j]  # 1 operation per step, key is saved separately


Does Your Version Still Work?
Yes — swapping achieves the same sorted result. The logic is sound. 
It's just not the canonical insertion sort and does ~3x more writes in the inner loop.
Your comment # swap every element... actually hints at this — classic insertion sort would say shift instead of swap.
"""

# Sorting
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Start from the second element, first element alone is trivially sorted
        for i in range(1, n):
            key = nums[i]
            
            # Compare key with elements to its left, moving backwards
            j = i-1
            while j >= 0 and key < nums[j]:
                # swap every element that is greater than the key one position to the right
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1
        
        return nums

# ---------------- -------------------------------------------- -----------------------------

# Shifting Method: ~This is the correct way, so study this.

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Start from the second element, first element alone is trivially sorted
        for i in range(1, n):
            key = nums[i] # Save the element to be inserted
            
            # Compare key with elements to its left, moving backwards
            j = i-1
            while j >= 0 and key < nums[j]:
                # shift every element that is greater than the key one position to the right
                nums[j+1] = nums[j]
                j -= 1
            
            # Place key in its correct position
            nums[j+1] = key

        return nums
    
