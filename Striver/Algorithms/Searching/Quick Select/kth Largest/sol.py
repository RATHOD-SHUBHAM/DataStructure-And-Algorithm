class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n - k

        startIdx = 0
        endIdx = n -1

        return self.quickSelect(startIdx, endIdx, nums, k, n)
    
    def quickSelect(self, startIdx, endIdx, nums, k, n):
        if startIdx > endIdx:
            return
        
        pivot = startIdx
        left = startIdx + 1
        right = endIdx

        while left <= right:
            
            if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
                self.swap(left, right, nums)
            
            if nums[left] <= nums[pivot]:
                left += 1
            
            if nums[right] >= nums[pivot]:
                right -= 1
        
        self.swap(pivot, right, nums)

        if right == k:
            return nums[right]
        elif right < k:
            startIdx = right + 1
            return self.quickSelect(startIdx, endIdx, nums, k, n)
        else:
            endIdx = right - 1
            return self.quickSelect(startIdx, endIdx, nums, k, n)

    def swap(self, i , j , nums):
        nums[i] , nums[j] = nums[j] , nums[i]

