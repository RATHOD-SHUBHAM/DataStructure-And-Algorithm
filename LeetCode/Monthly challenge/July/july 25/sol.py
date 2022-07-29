# TC: O(logn)
# Sc: O(1)

# 2 pointer binary search

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        first_occurance = self.binarySearch(nums, target, True)
        
        if first_occurance == -1:
            return [-1, -1]
        
        # IF i found the first occurance i can return the same idx as second
        second_occurance = self.binarySearch(nums, target, False)
        
        return [first_occurance, second_occurance]
    
    def binarySearch(self, nums, target, firstOccurance):
        left = 0
        right = len(nums) - 1
        
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else: # nums[mid] == target
                if firstOccurance:
                    # array is sorted and I am finding the first occurance
                    # so once i find the first occurance the value on its left should be smaller
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    else:
                        right = mid - 1
                # finding the second occurance
                else:
                    # array is sorted and I am finding the second occurance
                    # so once i find the second occurance the value on its right should be greater
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    else:
                        left = mid + 1
                        
        # if i dont find the occurance
        return -1
                        