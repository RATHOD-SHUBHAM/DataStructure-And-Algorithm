class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pos = len(nums) - k
        return self.helper(nums, 0 , len(nums) - 1, pos)
    
    def helper(self, nums, start, end, pos):
        # keep iterating until all the number are in right position
        while True:
            
            if start > end:
                break
                
            pivot = start
            left = start + 1
            right = end
            
            while left <= right:
                if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
                    self.swap(left, right, nums)
                    
                if nums[left] <= nums[pivot]:
                    left += 1
                    
                if nums[right] >= nums[pivot]:
                    right -= 1
                    
            self.swap(right, pivot, nums)
            
            if right == pos:
                return nums[right]
            elif right < pos:
                start = right + 1 # right is in correct place
            else:
                end = right - 1
                
                
    def swap(self, i , j , nums):
        nums[i] , nums[j] = nums[j], nums[i]
            
            
                
            
                
            