class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = [] # to get the order from string

        for i in s:
            # if opening bracket , add to stack
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                # if the first element itself is closing bracket
                if not stack:
                    return False

                brac = stack.pop()

                # Compare if the bracket matches
                if dic[i] != brac:
                    return False
        
        return True if stack == [] else False