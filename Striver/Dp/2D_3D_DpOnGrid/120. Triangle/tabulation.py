class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[-1])

        dp = [[math.inf for _ in range(n)]for _ in range(m)]
        dp[0][0] = triangle[0][0]

        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + triangle[i][0]

            for j in range(1,n):
                if len(triangle[i]) <= j:
                    break
                
                up = dp[i-1][j]
                up_left = dp[i-1][j-1]

                dp[i][j] = triangle[i][j] + min(up, up_left)
  
        return min(dp[-1])