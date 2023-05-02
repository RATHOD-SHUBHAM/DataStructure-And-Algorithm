# Tc: O(n^2) | Sc: O(n^2)

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        dp = [0] * (n + 1)
        dp[n] = 0 # this was the base case in recursion
        
        for i in reversed(range(n)):
            # copy the recurence
            minCost = float("inf")

            for j in range(i , n):
                cur_string = s[i : j + 1]

                if self.isPalindrome(cur_string):
                    cost = 1 + dp[j+1]

                    minCost = min(minCost , cost)
                    
            dp[i] = minCost
        
         # -1 becasue eg: aba - it will add a cut in end
        return  dp[0] - 1
    
    def isPalindrome(self, cur_string):
        reversed_str = cur_string[ : : -1]
        
        return cur_string == reversed_str