class Solution:
    def __init__(self):
        self.stack = []

        self.dic = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
    
    def isValid(self, s: str) -> bool:
        for x in s:
            if x == '(' or x == '{' or x == '[':
                self.stack.append(x)
            else:
                if not self.stack :
                    return False
                
                open_para = self.stack.pop()

                if open_para != self.dic[x]:
                    return False
        
        return False if self.stack else True