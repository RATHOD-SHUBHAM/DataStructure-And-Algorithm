class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2
        idx = n - 1
        
        return self.recursion(idx, nums, target)
    
    def recursion(self, idx, arr, target):
        # base case
        if idx == 0:
            if target == 0:
                return True
                
            if arr[0] == target:
                return True
            else:
                return False
        
        # Take
        if arr[idx] <= target:
            take = self.recursion(idx - 1, arr, target - arr[idx])
        else:
            take = False
        
        no_take = self.recursion(idx - 1, arr, target)
        
        return take or no_take