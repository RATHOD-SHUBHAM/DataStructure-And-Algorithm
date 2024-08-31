# Tc and Sc: O(n) 

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        # If i have to remove every element
        if k == n:
            return "0"

        stack = []

        for i in range(n):

            cur_ele = num[i]

            while stack and k > 0 and cur_ele < stack[-1]:
                stack.pop()
                k -= 1

            stack.append(cur_ele)

        
        # if stack only had increasing number
        while k > 0:
            stack.pop()
            k -= 1
        
        # If there are preceding zeros
        i = 0
        while i < len(stack):
            if stack[i] == '0':
                stack.pop(0)
            else:
                break

        return "".join(stack) if stack else "0"
    

# -----------------  Same solution different way  ------------------------

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        # If i have to remove every element
        if k == n:
            return "0"

        stack = []

        for i in range(n):

            cur_ele = num[i]

            while stack and k > 0 and cur_ele < stack[-1]:
                stack.pop()
                k -= 1

            stack.append(cur_ele)

        
        # if stack only had increasing number
        stack = stack[ : -k] if k > 0 else stack
        
        # If there are preceding zeros
        stack =  "".join(stack).lstrip('0') 
        
        if stack:
            return stack
        else:
            return "0"