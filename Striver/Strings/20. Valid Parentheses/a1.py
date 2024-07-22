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


# ---------------- Easy understanding ----------------

class Solution:
    def __init__(self):
        self.stack = []

    def isValid(self, s: str) -> bool:
        dic = {
            ')' : '(',
            '}' : '{',
            ']':'['
        }

        for para in s:
            if para == '(' or para == '[' or para == '{':
                self.stack.append(para)
            else:
                if not self.stack:
                    return False
                    
                open_para = self.stack.pop()

                if dic[para] != open_para:
                    return False
        
        return True if not self.stack else False

        