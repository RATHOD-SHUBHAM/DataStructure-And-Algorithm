class Solution:
    def rowWithMax1s(self, arr):
        # code here
        m = len(arr)
        n = len(arr[0])
        
        for col in range(n):
            for row in range(m):
                if arr[row][col] == 1:
                    return row
        
        return -1