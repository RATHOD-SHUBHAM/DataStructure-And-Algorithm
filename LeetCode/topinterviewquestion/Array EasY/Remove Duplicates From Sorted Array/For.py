# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return
        
        idx = 1
        
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx += 1
                
        return idx