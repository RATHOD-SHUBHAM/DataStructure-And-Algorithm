#  ------------------   Class function  ------------------

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
    

#  ------------------   Simple function  ------------------

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        op = []
        stack = []

        # Helper func
        def backTrack(i):
            if len(stack) == k:
                op.append(stack[:])
                return

            for j in range(i, n+1):
                stack.append(j)
                backTrack(j+1)
                stack.pop()
            
            return
        
        # Main Func
        backTrack(1)
        return op

