# What you’ve written is closer to selection sort (specifically, the swap-heavy variant sometimes called “exchange sort”)

#  What your code actually does: On each pass of i, 
# it scans the rest of the array and swaps whenever it finds something smaller than nums[i]. 
# By the end of the inner loop, position i holds the minimum of the remaining elements. 
# That “place the minimum at position i” invariant is the core idea of selection sort. 
# The difference is that true selection sort finds the index of the minimum first and does a single swap per pass, while yours may swap many times along the way.


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        
        return nums