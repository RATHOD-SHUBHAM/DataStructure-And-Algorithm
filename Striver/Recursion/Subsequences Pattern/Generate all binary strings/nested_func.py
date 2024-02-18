# Solution 1

class Solution:
    def __init__(self):
        self.result = []
        
    def generateBinaryStrings(self, n):
        # base case
        if n == 0:
            return self.result
        
        if n == 1:
            return ["0", '1']
            
        def dfs(st , n):
            # base case
            if n == 0:
                val = "".join(st) # convert list to string
                self.result.append(val)
                return
        
            # if the previous element is 0
            st.append("0")
            dfs(st, n - 1)
            st.pop()
            
            # now append 1
            if not st or st[-1] == "0":
                st.append("1")
                dfs(st, n - 1)
                st.pop()
            
            return
        
        # Function call
        st = []
        dfs(st, n)
        
        return self.result
    
# Solution 2 ----------------------------------------
    
class Solution:
    def __init__(self):
        self.result = []
        
    def generateBinaryStrings(self, n):
        # Code here
        if n == 1:
            return ["0" , "1"]
        
        def backTrack():
            if len(st) == n:
                val = "".join(st)
                self.result.append(val)
                return
        
            # Append 0
            st.append("0")
            backTrack()
            
            # Append 1
            st.pop()
            if not st or st[-1] == "0":
                st.append("1")
                backTrack()
                st.pop()
            
            return
        
        st = []
        backTrack()
        
        return self.result