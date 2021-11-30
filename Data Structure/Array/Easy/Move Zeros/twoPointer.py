class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0 
        
        for i in range(len(nums)):
            if nums[i] != 0:
                self.swap(nums, i , j)
                j += 1
        return nums
    
    def swap(self,nums,i,j):
        nums[i], nums[j] = nums[j], nums[i]