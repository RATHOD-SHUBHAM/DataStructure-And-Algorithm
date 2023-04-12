# Tc: O(n^2) | Sc: O(n^2)

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        start_idx = 0
        
        memo = [None] * n
        
        self.frontPartition(start_idx, memo, n, s)
        
         # -1 becasue eg: aba - it will add a cut in end
        return  memo[0] - 1
    
    def frontPartition(self, i, memo, n, s):
        # base case
        if i == n:
            return 0
        
        if memo[i]:
            return memo[i]
        
        # code
        minCost = float("inf")
        
        for j in range(i , n):
            cur_string = s[i : j + 1]
            
            if self.isPalindrome(cur_string):
                cost = 1 + self.frontPartition(j + 1, memo, n, s)
                
                minCost = min(minCost , cost)
                
        memo[i] = minCost
        return memo[i]
    
    def isPalindrome(self, cur_string):
        left = 0
        right = len(cur_string) - 1
        
        while left < right:
            if cur_string[left] != cur_string[right]:
                return False
            
            left += 1
            right -= 1
        
        return True