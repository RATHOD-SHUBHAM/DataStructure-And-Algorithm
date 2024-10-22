# Brute Force

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        left_array = [None] * n

        max_ele = -math.inf
        for i in range(n):
            cur_ele = nums[i]
            max_ele = max(max_ele, cur_ele)
            left_array[i] = max_ele
        
        max_ele = left_array[-1]

        idx = nums.index(max_ele)
        return idx

# ------------------------------------------------------------------------

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        max_ele = max(nums)
        idx = nums.index(max_ele)
        return idx