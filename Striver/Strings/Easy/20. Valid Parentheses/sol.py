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

        