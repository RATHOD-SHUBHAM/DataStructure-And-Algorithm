class Solution:
    def __init__(self):
        self.result = []
        
    def AllPossibleStrings(self, s):
        
        def backTrack(i, st):
            if i >= len(s):
                val = "".join(st)
                self.result.append(val)
                return
            
            # Include the current element
            st.append(s[i])
            backTrack(i+1, st)
            
            # Donot include current element
            st.pop()
            backTrack(i + 1, st)
            
            return
        
        st = []
        i = 0
        backTrack(i, st)
        
        return self.result