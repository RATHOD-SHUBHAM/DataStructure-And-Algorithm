# Time and Space = O(m * n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m , n = len(s1) , len(s2)
        
        # base case
        if len(s3) != m + n :
            return False
        
        # initialize 2D dp
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True # making the first element as True
        
        # Filling in row element for col 0
        for i in range(1 , m+1):
            # check the above value and current element
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        # print("first col")
        # print(dp)
        # print("\n")
            
        # filling in column element for row 0
        for j in range(1, n+1):
            # check to the left and current element
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        # print("first row: ")
        # print(dp)
        # print("\n")
            
        # fill in the remaining cells
        for i in range(1, m+1):
            # print("i",i)
            for j in range(1 , n+1):
                # print("j",j)
                chose_1 = chose_2 = False
                # if the current value from s1 match s3, check if the above cell value also match
                if s1[i-1] == s3[i+j-1]:
                    # if the value matches: check the above value
                    chose_1 = dp[i-1][j]
                    
                if s2[j-1] == s3[i+j-1]:
                    chose_2 = dp[i][j-1]
                    
                dp[i][j] = chose_1 or chose_2
                # print(dp)
                # print("\n")
                # print("----")
                
        return dp[-1][-1]
        