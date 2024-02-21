# Brute Force - Recursion - Memory Limit Exceed.
class Solution:
    def __init__(self):
        self.result = []

    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Get all the subsequence or original string
        def backTrack(i, st):
            # basecase
            if i >= len(t):
                val = "".join(st)
                self.result.append(val)
                return 
            
            # include the current element
            st.append(t[i])
            backTrack(i + 1, st)

            # donot include the current element
            st.pop()
            backTrack(i + 1, st)

            return

        
        st = []
        i = 0
        backTrack(i, st)

        # print(self.result)

        return True if s in self.result else False

# ------------------------------------------------------------------------------

# Two Pointer

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)

        p = q = 0

        while p < ns and q < nt:
            if s[p] == t[q]:
                p += 1
            
            q += 1
        
        return p == ns