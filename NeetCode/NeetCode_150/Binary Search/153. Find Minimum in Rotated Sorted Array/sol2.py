class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        # Number is already sorted
        if nums[left] < nums[right]:
            return nums[left]

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                if nums[mid] > nums[mid + 1]:
                    return nums[mid + 1]
                else:
                    left = mid + 1
            
            else:
                if nums[mid] < nums[mid - 1]:
                    return nums[mid]
                else:
                    right = mid - 1
        
        return nums[left]