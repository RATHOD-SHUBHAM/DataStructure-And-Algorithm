# ------------------------------------ Recursive Solution ------------------------------------

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        idx = 0
        count = 0 # keep the count of opening and closing bracket

        return self.recursion(idx, count, s, n)
    
    def recursion(self, idx, count, s, n):
        # base case
        if count == -1:
            """There is a closing bracket but no opening bracket"""
            return False
        
        if idx == n:
            if count == 0:
                # all the brackets were in proper pair
                return True
            else:
                return False
        
        # Logic
        if s[idx] == '(':
            # Increase the count by one -> this shows that there is a opening bracket on left
            return self.recursion(idx + 1, count + 1, s, n)
        
        elif s[idx] == ')':
            # Decrease the count bracket -> this shows that there is a closing bracket on left
            return self.recursion(idx + 1, count - 1, s, n)
        
        elif s[idx] == '*':
            """
                * can be assumed as
                1. Opening bracket
                2. Closing bracket
                3. Empty string
            """
            open_brac = self.recursion(idx + 1, count + 1, s, n)
            close_brack = self.recursion(idx + 1, count - 1, s, n)
            empt_str = self.recursion(idx + 1, count, s, n)

            # if any one is true, then we have found a valid paranthesis
            return open_brac or close_brack or empt_str


# ------------------------------------ Memo Solution ------------------------------------

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        idx = 0
        count = 0 # keep the count of opening and closing bracket

        memo = {}

        return self.recursion(idx, count, memo, s, n)
    
    def recursion(self, idx, count, memo, s, n):
        # base case
        if count == -1:
            """There is a closing bracket but no opening bracket"""
            return False
        
        if idx == n:
            if count == 0:
                # all the brackets were in proper pair
                return True
            else:
                return False
        
        if (idx, count) in memo:
            return memo[(idx, count)]
        
        # Logic
        if s[idx] == '(':
            # Increase the count by one -> this shows that there is a opening bracket on left
            memo[(idx, count)] = self.recursion(idx + 1, count + 1, memo, s, n)
            return memo[(idx, count)]
        
        elif s[idx] == ')':
            # Decrease the count bracket -> this shows that there is a closing bracket on left
            memo[(idx, count)] = self.recursion(idx + 1, count - 1, memo, s, n)
            return memo[(idx, count)]
        
        elif s[idx] == '*':
            """
                * can be assumed as
                1. Opening bracket
                2. Closing bracket
                3. Empty string
            """
            open_brac = self.recursion(idx + 1, count + 1, memo, s, n)
            close_brack = self.recursion(idx + 1, count - 1, memo, s, n)
            empt_str = self.recursion(idx + 1, count, memo, s, n)

            # if any one is true, then we have found a valid paranthesis
            memo[(idx, count)] = open_brac or close_brack or empt_str
            return memo[(idx, count)]

# ------------ Back to front ------------

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        idx = n - 1
        count = 0 # keep the count of opening and closing bracket

        memo = {}

        return self.recursion(idx, count, memo, s, n)
    
    def recursion(self, idx, count, memo, s, n):
        # base case
        if count == -1:
            """There is a closing bracket but no opening bracket"""
            return False
        
        if idx < 0:
            if count == 0:
                # all the brackets were in proper pair
                return True
            else:
                return False
        
        if (idx, count) in memo:
            return memo[(idx, count)]
        
        # Logic
        if s[idx] == '(':
            # Decrease the count bracket -> this shows that there is a opening bracket on right
            memo[(idx, count)] = self.recursion(idx - 1, count - 1, memo, s, n)
            return memo[(idx, count)]
        
        elif s[idx] == ')':
            # Increase the count bracket -> this shows that there is a closing bracket on right
            memo[(idx, count)] = self.recursion(idx - 1, count + 1, memo, s, n)
            return memo[(idx, count)]
        
        elif s[idx] == '*':
            """
                * can be assumed as
                1. Opening bracket
                2. Closing bracket
                3. Empty string
            """
            open_brac = self.recursion(idx - 1, count - 1, memo, s, n)
            close_brack = self.recursion(idx - 1, count + 1, memo, s, n)
            empt_str = self.recursion(idx - 1, count, memo, s, n)

            # if any one is true, then we have found a valid paranthesis
            memo[(idx, count)] = open_brac or close_brack or empt_str
            return memo[(idx, count)]

        
# ------------------------------------ Tabulation Solution ------------------------------------

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


# ------------------------------------ Wrong Solution ------------------------------------
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        dp = [[False for _ in range(n + 1)] for _ in range(n+1)]

        # base case
        for i in range(n+1):
            dp[i][0] = True # Assumption: string is always valid when count is zero
        
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

        # Keep track of the count for opening brackets
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
    
# ------------------------------------ Space Optimized ------------------------------------
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
    
# ----------------------------------- 2 Stack Solution -----------------------------------
# Tc: O(n)
# Sc: O(n)

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        open_para = [] # keep track of open parantheses
        ast = [] # keep track of asterisk3

        for i in range(n):
            if s[i] == '(':
                open_para.append(i)
            elif s[i] == '*':
                ast.append(i)
            else:
                if open_para:
                    open_para.pop()
                elif ast:
                    ast.pop()
                else:
                    return False
        
        while open_para and ast:
            para = open_para.pop()
            at = ast.pop()

            # Check if open para occured before *
            if para > at:
                return False
        
        return True if not open_para else False
    
# ---------------------------------Greedy Solution---------------------------------
# Tc: O(n)
# Sc: O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        # Track the range of possible open parentheses count
        min_open = 0  # minimum possible open parens -> best case scenario
        max_open = 0  # maximum possible open parens -> worst case scenario
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1

            elif char == ')':
                min_open -= 1
                max_open -= 1
            
            else:  # char == '*'
                # char - 1, char + 1, or char (empty string) -> so range = [-1, 0, +1]
                min_open -= 1  # treat as ')'
                max_open += 1  # treat as '('
            
            # If max_open becomes negative, we have too many ')' 
            if max_open == -1:
                return False
            
            # min_open should never go below 0
            if min_open == -1:
                min_open = 0

        
        # At the end, we need min_open to be 0 or less
        # (meaning it's possible to have 0 open parens)
        return min_open == 0
    
