class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        prev_max = grid[0]

        min_no_of_steps = 0
        
        for j in range(n):
            for i in range(1, m):
                cur_val = grid[i][j]
                diff = prev_max[j] - cur_val
                
                if diff < 0:
                    prev_max[j] = cur_val
                else:
                    min_no_of_steps += diff + 1
                    prev_max[j] = cur_val + diff+ 1

        return min_no_of_steps
            