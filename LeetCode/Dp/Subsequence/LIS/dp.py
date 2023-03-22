# TC: O(n)^2 | Sc: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [1, 2, 3, 4]
        n = len(nums)
        dp = [1] * n
        
        
        for curIdx in range(1, n):
            for prevIdx in range(curIdx):
                dontTake = 0 + dp[curIdx]
                dp[curIdx] = dontTake
                
                # the value has to be strictly increasing
                if nums[prevIdx] < nums[curIdx]:
                    take =  1 + dp[prevIdx]
                    dp[curIdx] = max(dp[curIdx] , take)
                    
                
                
                    
        return max(dp)