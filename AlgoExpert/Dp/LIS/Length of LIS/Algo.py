class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = [None for _ in range(len(nums))]
        # index : keep track of max element
        index = [None for _ in range(len(nums) + 1)]
        
        length = 0
        
        for idx, num in enumerate(nums):
            left = self.binarySearch(1, length, num, nums, index)
            
            sequence[idx] = index[left - 1]
            index[left] = idx
            
            length = max(length, left)
        
        return length
    
    def binarySearch(self,left, right, num, nums, index):
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[index[mid]] < num:
                left = mid + 1
            else:
                right = mid - 1
            
        return left