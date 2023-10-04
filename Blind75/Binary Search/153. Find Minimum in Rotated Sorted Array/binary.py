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

        # base condition
        # if there is only one element in array
        if n == 1:
            return nums[0]

        # if the array is not rotated
        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = n - 1

        min_array = self.binarySearch(left, right, nums, n)

        return min_array
    
    def binarySearch(self, left, right, nums, n):
        '''
        * We need to find 'Inflation Point'

        Stopping condition
            * nums[mid] > nums[mid + 1] Hence, mid+1 is the smallest.

            * nums[mid - 1] > nums[mid] Hence, mid is the smallest.
        '''

        while left < right:
            # Inflation point
            mid = left + (right - left) // 2

            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[left]:
                # all element in between left to mid are greater
                left = mid + 1
            
            else:
                right = mid - 1
