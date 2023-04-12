# Tc: O(2^n) | Sc: O(n)

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        start_idx = 0
        
        min_cut = self.frontPartition(start_idx, n, s)
        
         # -1 becasue eg: aba - it will add a cut in end
        return  min_cut - 1
    
    def frontPartition(self, i, n, s):
        # base case
        if i == n:
            return 0
        
        # code
        minCost = float("inf")
        
        for j in range(i , n):
            cur_string = s[i : j + 1]
            
            if self.isPalindrome(cur_string):
                cost = 1 + self.frontPartition(j + 1, n, s)
                
                minCost = min(minCost , cost)
                
        return minCost
    
    def isPalindrome(self, cur_string):
        left = 0
        right = len(cur_string) - 1
        
        while left < right:
            if cur_string[left] != cur_string[right]:
                return False
            
            left += 1
            right -= 1
        
        return True