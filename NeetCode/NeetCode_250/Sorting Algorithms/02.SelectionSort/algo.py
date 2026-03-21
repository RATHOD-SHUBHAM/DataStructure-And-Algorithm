"""
Selection Sort: 
Core Idea: 
Divide the array into two parts: sorted (left) and unsorted (right). 
In each pass, find the minimum element from the unsorted part and place it at the beginning of the unsorted part. 
Move the sorted boundary.
Repeat until the whole array is sorted.

Tc and Sc: O(n^2)
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i = 0

        while i < n:
            min_idx = i

            for j in range(i, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            
            # swap
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

            i += 1
        
        return nums