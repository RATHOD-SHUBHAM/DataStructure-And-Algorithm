class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # find out where the largest kth element will be present in array
        pos = len(nums) - k
        # assign the start and end value
        return self.quickSelect(0, len(nums) - 1, pos, nums)
    
    def quickSelect(self, start, end, pos, nums):
        while True:
            
            if start > end:
                break
                
            pivot = start
            left = start + 1
            right = end
            
            while left <= right:
                # all the elements to left will be less than pivot and element to right will be greater than or equal to pivot
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
                start = right + 1 # right is in its proper position
            else:
                end = right - 1
                
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j] , nums[i]