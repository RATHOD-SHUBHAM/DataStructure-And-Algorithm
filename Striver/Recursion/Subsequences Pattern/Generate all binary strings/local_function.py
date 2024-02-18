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
    
# Solution 2 ----------------------------------------

class Solution:
    def __init__(self):
        self.result = []
        self.st = []
        
    def generateBinaryStrings(self, n):
        # Code here
        if n == 1:
            return ["0" , "1"]
        
        self.backTrack(n)
        
        return self.result
    
    def backTrack(self, n):
        # base case
        if len(self.st) == n:
            val = "".join(self.st)
            self.result.append(val)
            return
    
        # Append 0
        self.st.append("0")
        self.backTrack(n)
        self.st.pop()
        
        # Append 1
        if not self.st  or self.st[-1] == "0":
            self.st.append("1")
            self.backTrack(n)
            self.st.pop()
        
        return