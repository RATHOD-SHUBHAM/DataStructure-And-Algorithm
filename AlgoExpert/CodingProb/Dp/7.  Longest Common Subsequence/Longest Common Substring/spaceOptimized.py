class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        m = len(S1)
        n = len(S2)
        
        prev = [0 for _ in range(n + 1)]
        cur = [0 for _ in range(n + 1)]
        
        res = 0
        
        for i in range(1, m + 1):
            for j in range(1 , n + 1):
                if S1[i - 1]== S2[j - 1]:
                    cur[j] = 1 + prev[j-1]
                    res = max(res, cur[j])
                else:
                    cur[j] = 0
                    
            
            prev = [x for x in cur]
        

        return res