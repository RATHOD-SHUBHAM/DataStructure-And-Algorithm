# Tc and Sc: O(n)

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        curPos = start
        return self.dfs(curPos, arr)
    
    def dfs(self, curPos, arr):
        # base case
        # index out of bound or if vertex is already visited
        if curPos < 0 or curPos >= len(arr) or arr[curPos] < 0:
            return False
        
        # if this is the end position
        if arr[curPos] == 0:
            return True
        
        # mark the vertex as visited
        arr[curPos] *= -1
        
        # DfS call
        jumpFront = self.dfs(curPos + arr[curPos], arr)
        jumpBack = self.dfs(curPos - arr[curPos], arr)
        
        return jumpFront or jumpBack