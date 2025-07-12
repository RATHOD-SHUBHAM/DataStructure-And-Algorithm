# ------------------- Recursion -------------------
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[-1])

        min_path_sum = math.inf
        i = m - 1
        for j in reversed(range(n)):
            cur_path_sum = self.recursion(i, j, triangle)
            min_path_sum = min(min_path_sum, cur_path_sum)
        
        return min_path_sum
    
    def recursion(self, i, j, grid):
        # base case
        if i == 0 and j == 0:
            return grid[0][0]
        
        if i < 0 or j < 0 or j >= len(grid[i]):
            return math.inf
        
        # Logic
        up = self.recursion(i - 1, j, grid)
        left = self.recursion(i - 1, j - 1, grid)

        return grid[i][j] + min(up, left)

# ------------------- Memoization -------------------
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[-1])

        min_path_sum = math.inf
        i = m - 1
        for j in reversed(range(n)):
            cur_path_sum = self.recursion(i, j, {}, triangle)
            min_path_sum = min(min_path_sum, cur_path_sum)
        
        return min_path_sum
    
    def recursion(self, i, j, memo, grid):
        # base case
        if i == 0 and j == 0:
            return grid[0][0]
        
        if i < 0 or j < 0 or j >= len(grid[i]):
            return math.inf
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Logic
        up = self.recursion(i - 1, j,memo, grid)
        left = self.recursion(i - 1, j - 1, memo, grid)

        memo[(i, j)] = grid[i][j] + min(up, left)

        return memo[(i, j)]

# ------------------- Tabulation -------------------
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[-1])

        dp = [[math.inf for _ in range(n)]for _ in range(m)]
        dp[0][0] = triangle[0][0]

        for i in range(1, m):
            for j in range(n):
                if j >= len(triangle[i]):
                    continue

                up = dp[i-1][j]
                left = dp[i-1][j-1] if j - 1 >= 0 else math.inf

                dp[i][j] = triangle[i][j] + min(up, left)
        
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