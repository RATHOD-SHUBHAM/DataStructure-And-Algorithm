# ------------------- Recursion -------------------
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[0])

        row = 0
        col = 0

        return self.recursion(row, col, m, n, triangle)
    
    def recursion(self, row, col, m, n, triangle):
        # base case
        if row >= m:
            return 0
        
        down = self.recursion(row+1, col, m, n, triangle)
        down_right = self.recursion(row+1, col+1, m, n, triangle)

        cur_path_sum = triangle[row][col] + min(down, down_right)

        return cur_path_sum

# ------------------- Memoization -------------------
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[0])

        row = 0
        col = 0

        memo = {}

        return self.recursion(row, col, memo, m, n, triangle)
    
    def recursion(self, row, col, memo, m, n, triangle):
        # base case
        if row >= m:
            return 0
        
        if (row, col) in memo:
            return memo[(row,col)]
        
        down = self.recursion(row+1, col, memo, m, n, triangle)
        down_right = self.recursion(row+1, col+1, memo, m, n, triangle)

        cur_path_sum = triangle[row][col] + min(down, down_right)

        memo[(row,col)] = cur_path_sum

        return memo[(row,col)]

# ------------------- Tabulation -------------------
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
    
# ------------------- Space Optimization -------------------
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