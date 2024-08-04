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
