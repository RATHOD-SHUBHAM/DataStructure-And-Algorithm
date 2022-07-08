# Time = O(m * n)
# space = O(min(m,n))
# first try making a 2D array then simplify it into one D
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m , n = len(s1) , len(s2)
        
        if len(s3) != m + n : 
            return False
        
        # making sure s2 is smaller than s1
        if m < n:
            m , n = n , m
            s1 , s2 = s2 , s1
            
        dp = [False] * (n + 1)
        dp[0] = True
        
        # filling the col value for first row
        for i in range(1, n+1):
            dp[i] = dp[i-1] and s2[i-1] == s3[i-1]
            
        # filling in the remaining cell
        for i in range(1 , m+1):
            # fill in the first cell
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            
            for j in range(1, n + 1):
                chose_1 = chose_2 = False
                
                if s1[i-1] == s3[i+j-1]:
                    chose_1 = dp[j]
                    
                if s2[j-1] == s3[i+j-1]:
                    chose_2 = dp[j-1]
                    
                dp[j] = chose_1 or chose_2
                
        return dp[-1]