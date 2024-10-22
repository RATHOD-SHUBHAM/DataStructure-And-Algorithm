# Divide the search space into left or right half

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        peak = self.checkPeak(left, right, n, nums)

        return peak
    
    def checkPeak(self, left, right, n, nums):
        if left > right:
            return 0
        
        mid = left + (right - left) // 2

        # Edge
        if (mid - 1 == -1 or nums[mid] > nums[mid - 1]) and (mid + 1 == n or nums[mid] > nums[mid + 1]):
            return mid
        
        move_left = self.checkPeak(left, mid - 1, n, nums)
        move_right = self.checkPeak(mid + 1, right, n, nums)

        if move_left == 0:
            return move_right
        else:
            return move_left