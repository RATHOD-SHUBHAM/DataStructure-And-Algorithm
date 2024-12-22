# -------------------------- Brute Force Solution --------------------

class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        MOD = (10 ** 9) + 7

        # --------------------------

        def dfs(i, j, xor_sum):
            if i >= m or j >= n:
                return 0

            # Add the current grid value
            xor_sum = grid[i][j] ^ xor_sum


            if i == m - 1 and j == n - 1:
                if xor_sum == k:
                    return 1
                else:
                    return 0


            # Move Right
            right_path_sum = dfs(i, j + 1, xor_sum)
            
            # Move Down
            down_path_sum = dfs(i + 1, j, xor_sum)

            return (right_path_sum + down_path_sum) % MOD

        # --------------------------
        i = 0
        j = 0
        xor_sum = 0
        no_of_path = dfs(i, j, xor_sum)

        return no_of_path % MOD
    
# -------------------------- Optimal Solution --------------------


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        MOD = (10 ** 9) + 7

        memo = {}

        # --------------------------

        def dfs(i, j, xor_sum):
            if i >= m or j >= n:
                return 0

            # Add the current grid value
            xor_sum = grid[i][j] ^ xor_sum


            if i == m - 1 and j == n - 1:
                if xor_sum == k:
                    return 1
                else:
                    return 0
            
            if (i, j, xor_sum) in memo:
                return memo[(i, j, xor_sum)]


            # Move Right
            right_path_sum = dfs(i, j + 1, xor_sum)
            
            # Move Down
            down_path_sum = dfs(i + 1, j, xor_sum)

            memo[(i, j, xor_sum)] = (right_path_sum + down_path_sum) % MOD
            return memo[(i, j, xor_sum)]

        # --------------------------
        i = 0
        j = 0
        xor_sum = 0
        no_of_path = dfs(i, j, xor_sum)

        return no_of_path % MOD