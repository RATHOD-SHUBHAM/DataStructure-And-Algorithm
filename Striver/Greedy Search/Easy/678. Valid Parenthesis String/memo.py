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

        
        