'''
    Trick:
        * If the array is not rotated and the array is in ascending order, then 
            last element > first element
            eg: 1,2,3,4,5: 
                5 > 1

        * If the array is rotated,then
            last element < first element
            eg: 3,4,5,1,2
                2 < 3
'''

# Tc : O(logn) | Sc: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        # Check if the array is already sorted
        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                if nums[mid] > nums[mid + 1]:
                    return nums[mid + 1]
                else:
                    left = mid + 1
            else:
                if nums[mid] > nums[left]:
                    return nums[left]
                else:
                    right = mid
        
        return nums[left]