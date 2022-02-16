# Brute Force

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : x[1])
        # print(envelopes)
        
        dp = [1 for _ in range(len(envelopes))]
        
        for i in range(1,len(envelopes)):
            cur_env = envelopes[i]
            
            for j in range(i):
                prev_env = envelopes[j]
                
                if prev_env[0] < cur_env[0] and prev_env[1] < cur_env[1]:
                    dp[i] = max(dp[i] , dp[j]+1)
        # print(dp)
        
        return max(dp)
                    
                