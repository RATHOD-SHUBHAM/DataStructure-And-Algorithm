# Tc and Sc : O(n)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k > len(num):
            return
        
        stack = [] # monotonic stack
        
        for i in range(len(num)):
            while k != 0 and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            
            stack.append(num[i])
            
        while k != 0:
            stack.pop()
            k -= 1
            
    
        return "".join(stack).lstrip('0') or "0"
