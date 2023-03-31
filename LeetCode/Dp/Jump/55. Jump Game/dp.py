# Tc:O(n^2) | Sc:O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True
        
        for curIdx in reversed(range(n-1)):
            max_rechableIdx = curIdx + nums[curIdx] # maximum distance i can travell from current idx
            for rechableIdx in range(curIdx + 1, max_rechableIdx + 1):
                # check if from this position I can reach the end
                if dp[rechableIdx] == True:
                    dp[curIdx] = True
                    break
                    
        return dp[0] == True