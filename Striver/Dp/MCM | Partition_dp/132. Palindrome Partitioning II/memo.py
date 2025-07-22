class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        i = 0

        memo = {}

        return self.recursion(i, n, memo, s)
    
    def recursion(self, i, n, memo, s):
        # base case
        if i == n:
            return -1 # we nullify the last cut
        
        if (i, s) in memo:
            return memo[(i, s)]
        
        # logic
        min_cuts = math.inf

        for j in range(i, n):
            cur_str = s[i: j+1]

            if self.isPali(cur_str):
                cur_cost = 1 + self.recursion(j+1, n, memo, s)
                min_cuts = min(min_cuts, cur_cost)
        
        memo[(i, s)] = min_cuts
        return min_cuts
    
    def isPali(self, arr):
        i = 0
        j = len(arr) - 1

        while i <= j:
            if arr[i] != arr[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
