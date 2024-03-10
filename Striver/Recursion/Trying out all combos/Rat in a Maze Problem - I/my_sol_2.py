class Solution:
    def __init__(self):
        self.paths = []
        
    def findPath(self, m, n):
        
        visited = [[False for _ in range(n)] for _ in range(n)]
        
        if m[0][0] == 0:
            return [-1]
        
        cur_path = []
        self.backTrack(0, 0, cur_path, visited, m ,n)
        
        if not self.paths:
            return [-1]
        
        return self.paths
    
    def backTrack(self, row, col, cur_path, visited, m , n):
        # basecase
        if row < 0 or row >= n or col < 0 or col >= n or visited[row][col] == True or m[row][col] == 0:
            return
            
        if row == n - 1 and col == n - 1:
            val = "".join(cur_path)
            self.paths.append(val)
            return
        
        visited[row][col] = True
        
        up = self.backTrack(row - 1, col, cur_path + ['U'], visited, m ,n)
        down = self.backTrack(row + 1, col, cur_path + ['D'], visited, m ,n)
        left = self.backTrack(row, col - 1, cur_path + ['L'], visited, m ,n)
        right = self.backTrack(row, col + 1, cur_path + ['R'], visited, m ,n)
        
        visited[row][col] = False
        
        return 


if __name__ == '__main__':
    n = 4
    m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    
    obj = Solution()

    print(obj.findPath(m,n))
