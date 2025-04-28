class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[-1])

        dp = [math.inf for _ in range(n)]
        dp[0] = triangle[0][0]

        for i in range(1,m):
            temp = [math.inf for _ in range(n)]
            temp[0] = dp[0] + triangle[i][0]

            for j in range(1,n):
                if len(triangle[i]) <= j:
                    break
                
                up = dp[j]
                up_left = dp[j-1]

                temp[j] = triangle[i][j] + min(up, up_left)
            
            dp = temp
  
        return min(dp)