class Solution:
    def __init__(self):
        self.result = []
        self.st = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backTrack(start):
            # base case
            if len(self.st) == k:
                self.result.append(self.st.copy())
                return
            
            for i in range(start, n + 1):
                self.st.append(i)
                backTrack(i + 1)
                self.st.pop()
            
            return
        
        start = 1
        backTrack(start)

        return self.result

# ------------------------------------------------------------------------------
# Optimized local Function   

class Solution:
    def __init__(self):
        self.result = []
        self.st = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        start = 1
        self.backTrack(start, n, k)

        return self.result
    
    def backTrack(self, start, n , k):
        # base case
        if len(self.st) == k:
            self.result.append(self.st.copy())
            return
        
        # Move across and add each element
        for i in range(start, n+1):
            self.st.append(i)
            self.backTrack(i + 1, n, k)
            self.st.pop()
        
        return

        