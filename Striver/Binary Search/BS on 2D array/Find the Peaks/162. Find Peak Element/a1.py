# ----------------- One Pass -----------------

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if i == 0 and nums[i+1] < nums[i]:
                return i

            if i == n-1 and nums[i-1] < nums[i]:
                return i

            elif nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                return i


# ----------------- Binary Search -----------------

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # Edge Case
        if n <= 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        
        if nums[n-1] > nums[n-2]:
            return n - 1
        

        # Binary Search
        left = 1
        right = n - 2

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            
            # Peak is on right side
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # nums[mid - 1] > nums[mid] ; Peak will be on the left
                right = mid - 1
        