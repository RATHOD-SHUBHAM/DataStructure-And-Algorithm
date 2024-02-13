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