"""
Wrong Solution:
Issue 1: Wrong Base Case
code:
for i in range(n+1):
    dp[i][0] = True # string is always valid when count is zero

Problem: This is incorrect! A string is NOT always valid when count is 0.

What it should be: Only when we've processed ALL characters (idx = n) AND count = 0, then it's valid.
Correct base case:
dp[0][0] = True  # Only this should be True initially

Issue 2: Wrong Return Statement
return dp[n][n]  # WRONG!

Problem: You want dp[n][0], not dp[n][n]. You're looking for the case where you've processed all characters and the count is 0.

return dp[n][0]  # CORRECT!

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        dp = [[False for _ in range(n + 1)] for _ in range(n+1)]

        # base case
        for i in range(n+1):
            dp[i][0] = True # string is always valid when count is zero
        
        for idx in range(1, n+1):
            for count in range(1, n+1):
                # Logic
                if s[idx - 1] == '(':
                    # Decrease the count bracket -> this shows that there is a opening bracket on right
                    dp[idx][count] = dp[idx - 1][count - 1]
        
                elif s[idx - 1] == ')':
                    # Increase the count bracket -> this shows that there is a closing bracket on right
                    if count + 1 <= n:
                        dp[idx][count] = dp[idx - 1][count + 1]
                    else:
                        dp[idx][count] = False
        
                elif s[idx - 1] == '*':
                    open_brac = dp[idx - 1][count - 1]
                    
                    close_brack = False
                    if count + 1 <= n:
                        close_brack = dp[idx - 1][count + 1]
                    
                    empt_str = dp[idx - 1][count]

                    # if any one is true, then we have found a valid paranthesis
                    dp[idx][count] = open_brac or close_brack or empt_str
        
        print(dp)
        return dp[n][n]
    

# -------------------------------- Correct Solution --------------------------------
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        dp = [[False for _ in range(n + 1)] for _ in range(n+1)]

        # base case
        dp[0][0] = True
        
        for idx in range(1, n+1):
            for count in range(n+1):
                # Logic
                if s[idx - 1] == '(':
                    # Decrease the count bracket -> this shows that there is a opening bracket on right
                    if count - 1 >= 0:
                        dp[idx][count] = dp[idx - 1][count - 1]
                    else:
                        dp[idx][count] = False
        
                elif s[idx - 1] == ')':
                    # Increase the count bracket -> this shows that there is a closing bracket on right
                    if count + 1 <= n:
                        dp[idx][count] = dp[idx - 1][count + 1]
                    else:
                        dp[idx][count] = False
        
                elif s[idx - 1] == '*':
                    open_brac = False
                    if count - 1 >= 0:
                        open_brac = dp[idx - 1][count - 1]
                    else:
                        open_brac = False
                    
                    close_brack = False
                    if count + 1 <= n:
                        close_brack = dp[idx - 1][count + 1]
                    
                    empt_str = dp[idx - 1][count]

                    # if any one is true, then we have found a valid paranthesis
                    dp[idx][count] = open_brac or close_brack or empt_str
        
        # print(dp)
        # You're looking for the case where you've processed all characters and the count is 0.
        return dp[n][0]