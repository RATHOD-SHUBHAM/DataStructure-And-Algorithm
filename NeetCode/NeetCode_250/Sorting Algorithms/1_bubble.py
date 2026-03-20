"""
Bubble Sort: 
Core Idea: 
Walk through the array comparing two neighbors at a time. If the left is bigger than the right, swap them. 
Repeat until no swaps are needed. Large elements bubble up to the end with each pass.

Tc and Sc: O(n**2)
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for _ in range(n):
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            
        return nums