class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        i = 0

        return self.recursion(i, n, s)
    
    def recursion(self, i, n, s):
        # base case
        if i == n:
            return 0 # we nullify the last cut
        
        # logic
        min_cuts = math.inf

        for j in range(i, n-1):
            cur_str = s[i: j+1]

            if self.isPali(cur_str):
                cur_cost = 1 + self.recursion(j+1, n, s)
                min_cuts = min(min_cuts, cur_cost)
        
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
