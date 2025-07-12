class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [math.inf for _ in range(n)]

        # basecase
        for j in range(n):
            dp[j] = matrix[0][j]
        
        for i in range(1, m):
            cur = [math.inf for _ in range(n)]
            for j in range(n):
                # Logic
                up = dp[j]
                left = dp[j-1] if j-1 >= 0 else math.inf
                right = dp[j+1] if j+1 < n else math.inf

                cur[j] = matrix[i][j] + min(up, left, right)
            
            dp = cur
        
        return min(dp)