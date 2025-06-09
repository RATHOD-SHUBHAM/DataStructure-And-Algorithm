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

        