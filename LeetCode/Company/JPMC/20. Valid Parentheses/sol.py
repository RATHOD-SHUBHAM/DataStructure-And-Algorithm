class Solution:
    def __init__(self) -> None:
        self.stack = []

        self.dic = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

    def isValid(self, s: str) -> bool:
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                self.stack.append(ch)
            else:
                # Closing bracket
                if not self.stack:
                    return False
                
                brack = self.dic[ch]
                opening_brack = self.stack.pop()
                

                if brack != opening_brack:
                    return False
            
        return True if not self.stack else False

                
