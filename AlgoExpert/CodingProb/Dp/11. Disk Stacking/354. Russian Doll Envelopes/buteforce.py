# Brute Force

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        
        envelopes.sort(key = lambda x : x[1])
        # print(envelopes)
        
        stack = [1] * n
        
        for i in range(1, n):
            curEnv = envelopes[i]
            
            for j in range(0 , i):
                prevEnv = envelopes[j]
                
                if prevEnv[0] < curEnv[0] and prevEnv[1] < curEnv[1]:
                    
                    if stack[i] < 1 + stack[j]:
                        stack[i] = 1 + stack[j]
                        
        return max(stack)
                