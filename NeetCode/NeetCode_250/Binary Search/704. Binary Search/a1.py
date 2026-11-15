"""
* bisect_left(nums, t) returns the first index i where nums[i] >= t.

* bisect_right(nums, t) returns the first index i where nums[i] > t. 

Its important to check bound guard for both, because sometime i can be greater than len(nums)

# Left
# bounds guard
        if idx >= len(nums):
            return -1

            
# Right
# bounds guard
        if idx - 1 < 0:
            return -1
"""

# =========================================== Bisect Left ===========================================

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        idx = bisect.bisect_left(nums, target)

        # bounds guard
        if idx >= len(nums):
            return -1

        if nums[idx] == target: # nums[i] >= t
            return idx
        else:
            return -1

# =========================================== Bisect Right ===========================================
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        idx = bisect.bisect_right(nums, target)

        # bounds guard
        if idx - 1 < 0:
            return -1

        if nums[idx-1] == target: # nums[i] > t
            return idx - 1
        else:
            return -1

# =========================================== Binary Search ===========================================
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            # print(mid)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1