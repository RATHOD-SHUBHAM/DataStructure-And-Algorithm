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

        for i in range(n):
            min_idx = i

            # Find the index of the minimum element in the unsorted part
            for j in range(i, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            
            
            # Swap the found minimum element with the first element of the unsorted part
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            
            """
            # You could also do this
            if i != min_idx:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]
            """
        
        return nums