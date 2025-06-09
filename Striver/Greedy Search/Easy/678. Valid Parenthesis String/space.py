class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        dp = [False for _ in range(n + 1)]

        # base case
        dp[0] = True
        
        for idx in range(1, n+1):
            temp = [False for _ in range(n + 1)]

            for count in range(n+1):
                # Logic
                if s[idx - 1] == '(':
                    # Decrease the count bracket -> this shows that there is a opening bracket on right
                    if count - 1 >= 0:
                        temp[count] = dp[count - 1]
                    else:
                        temp[count] = False
        
                elif s[idx - 1] == ')':
                    # Increase the count bracket -> this shows that there is a closing bracket on right
                    if count + 1 <= n:
                        temp[count] = dp[count + 1]
                    else:
                        temp[count] = False
        
                elif s[idx - 1] == '*':
                    open_brac = False
                    if count - 1 >= 0:
                        open_brac = dp[count - 1]
                    else:
                        open_brac = False
                    
                    close_brack = False
                    if count + 1 <= n:
                        close_brack = dp[count + 1]
                    
                    empt_str = dp[count]

                    # if any one is true, then we have found a valid paranthesis
                    temp[count] = open_brac or close_brack or empt_str
                
            dp = temp

        # You're looking for the case where you've processed all characters and the count is 0.
        return dp[0]