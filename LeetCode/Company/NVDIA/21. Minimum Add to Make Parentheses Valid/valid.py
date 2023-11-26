# Tc :O(n) | Sc: O(1)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        dic = {
            ')' : '('
        } # Constant space

        stack = [] # will always be less than ip
        count = 0

        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if not stack:
                    count += 1
                    continue

                para = stack.pop()
                if dic[i] == para:
                    continue
        
        count += len(stack)
        return count
