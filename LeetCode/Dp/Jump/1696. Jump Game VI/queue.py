# Tc and Sc: O(n)
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        score = [0] * n # hold all the score
        score[0] = nums[0] 
        
        # keep track of current max score in the window of k
        dq = deque()
        # dp[0] will always hold the maximum value followed by others
        dq.append(0)
        
        for i in range(1, n):
            # Remove all the value which is not within the window range
            while dq and dq[0] < i - k:
                dq.popleft()
            
            score[i] = score[dq[0]] + nums[i]
            
            # if the current score is greater than the max value in q. then pop those value
            while dq and score[i] >= score[dq[-1]]:
                dq.pop()
            
            dq.append(i)
            
        return score[-1]