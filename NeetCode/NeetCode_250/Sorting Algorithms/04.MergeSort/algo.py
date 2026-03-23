"""
Merge Sort:
Core Idea:
Divide the array in half recursively until you have single elements
(which are trivially sorted), then merge them back together in sorted order.

TC: O(n log n) - log n levels of division, n work to merge at each level
SC: O(n) - temporary arrays used during merging
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            return merge(left, right)
        
        return mergeSort(nums)