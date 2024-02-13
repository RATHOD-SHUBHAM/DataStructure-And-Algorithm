class Solution:
    def __init__(self):
        self.result = []
        
    def generateBinaryStrings(self, n):
        if n == 0:
            return []
            
        if n == 1:
            return ["0", "1"]
            
        s = []
        self.dfs(s, n)
        
        return self.result
        
    def dfs(self, s , n):
        if n == 0:
            self.result.append("".join(s))
            return
        
        # First append "0"
        s.append("0")
        self.dfs(s, n - 1)
        s.pop()
        
        # Append 1
        if not s or s[-1] != '1':
            s.append("1")
            self.dfs(s, n - 1)
            s.pop()
        
        return