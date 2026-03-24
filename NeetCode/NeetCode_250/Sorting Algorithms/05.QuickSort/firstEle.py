"""
Why This Solution Gives TLE?
The issue is pivot selection — always choosing the first element as pivot.
When the array is already sorted (or nearly sorted), this creates worst-case O(n²) behavior:
[1, 2, 3, 4, 5]
pivot=1 → left=[], right=[2,3,4,5]   # unbalanced!
pivot=2 → left=[], right=[3,4,5]      # unbalanced again!
pivot=3 → left=[], right=[4,5]        # every single time...
Instead of O(n log n) splits, you get O(n) levels → O(n²) total.

Your "smaller side first" optimization doesn't help here because the imbalance itself is the problem — 
you can't optimize around a pivot that's always wrong.

"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        startIdx = 0
        endIdx = n - 1
        self.quickSort(nums, startIdx, endIdx)

        return nums

    def quickSort(self, nums, startIdx, endIdx):
        # Check if there is only element in array
        if startIdx >= endIdx:
            return
        
        # Pivot element
        pivot = startIdx
        left = startIdx + 1
        right = endIdx

        # Sort the array so that every element smaller than the pivot goes to its left and every element larger goes to its right. 
        while left <= right:
            if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
                """
                If left ele is greater than pivot and right ele is smaller than pivot -> swap them
                why?
                because every element smaller than the pivot goes to its left and every element larger goes to its right.
                """
                self.swap(nums, left, right)
            
            # Adjust your pointers as per the rule
            if nums[left] <= nums[pivot]:
                left += 1
            
            if nums[right] >= nums[pivot]:
                right -= 1
        
        # place the pivot in its correct final position
        self.swap(nums, pivot, right)

        # Recursively apply quick sort on the left side and right side
        smaller_side = (right - 1) - startIdx <= endIdx - (right + 1)

        if smaller_side:
            self.quickSort(nums, startIdx, right - 1)
            self.quickSort(nums, right+1, endIdx)
        else:
            self.quickSort(nums, right+1, endIdx)
            self.quickSort(nums, startIdx, right - 1)
    

    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]