class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        dp = [-1 for _ in range(n+1)]
        
        for i in reversed(range(0,n)):
            
            min_cuts = math.inf
            for j in range(i, n):
                
                cur_str = s[i: j+1]

                if self.isPali(cur_str):
                    cur_cost = 1 + dp[j+1]
                    min_cuts = min(min_cuts, cur_cost)
            
            dp[i] = min_cuts
        
        return dp[0]
    
    def isPali(self, arr):
        i = 0
        j = len(arr) - 1

        while i <= j:
            if arr[i] != arr[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
