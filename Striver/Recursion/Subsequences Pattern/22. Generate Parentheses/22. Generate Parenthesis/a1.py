# Nested Function

class Solution:
    def __init__(self):
        self.result = []
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(st, openCount, closedCount):
            # base case
            if openCount == closedCount == n:
                combo = "".join(st)
                self.result.append(combo)
                return
            
            # Append "("
            if openCount < n:
                st.append("(")
                dfs(st, openCount + 1, closedCount)
                st.pop()

            # Append ")"
            if closedCount < openCount:
                st.append(")")
                dfs(st , openCount, closedCount + 1)
                st.pop()
            
            return

        
        # Function call
        st = []
        openCount = closedCount = 0
        dfs(st, openCount , closedCount)

        return self.result
    

# ------------------------------------------------------------------------
    
class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        openCount = closedCount = 0
        self.dfs(st, openCount, closedCount, n)

        return self.result
    
    def dfs(self, st, openCount, closedCount, n):
        # base case
        if openCount == closedCount == n:
            combo = "".join(st)
            self.result.append(combo)
            return self.result
        
        # Append "("
        if openCount < n:
            st.append("(")
            self.dfs(st, openCount + 1, closedCount, n)
            st.pop()
        
        # Append ")"
        if closedCount < openCount:
            st.append(")")
            self.dfs(st, openCount, closedCount + 1, n)
            st.pop()
        
        return
