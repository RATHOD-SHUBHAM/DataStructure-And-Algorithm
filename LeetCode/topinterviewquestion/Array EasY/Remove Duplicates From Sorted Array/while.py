# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        i = 1
        idx = 1
        
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx += 1
                
            i += 1
            
        return idx #cause ill have to return the actual length