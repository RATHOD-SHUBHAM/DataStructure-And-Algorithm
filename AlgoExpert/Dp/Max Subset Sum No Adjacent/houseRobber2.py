# Tc: O(N) | Sc: O(1)

class Solution:
    def houseRobber(self, nums):
        n = len(nums)
        
        if n == 0:
            return 0
        
        if n == 1:
            return nums[0]
        
        non_adj = nums[0]
        adj = max(nums[0] , nums[1])
        
        for i in range(2, n):
            dontTake = 0 + adj
            take = nums[i] + non_adj
            
            cur = max(take, dontTake)
            
            non_adj = adj
            adj = cur
            
        
        return adj
    
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        
        if n == 1:
            return nums[0]
        
        nums_1 = nums[0 : n - 1]
        
        nums_2 = nums[1 : n]
        
        first = self.houseRobber(nums_1)
        second = self.houseRobber(nums_2)
        
        return max(first, second) 