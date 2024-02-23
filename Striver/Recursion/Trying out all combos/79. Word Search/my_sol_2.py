class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        curChar = 0 # to match the char of board to the char of word


        for row in range(m):
            for col in range(n):
                if board[row][col] != word[curChar]:
                    continue
                
                match = self.backTrack(row,col, m, n, visited, curChar, board, word)

                if match == True:
                    return True
        
        return False

    
    def backTrack(self, row, col, m, n , visited, curChar, board, word):
        # basecase
        if curChar == len(word):
            return True

        if row < 0 or row >= m or col < 0 or col >= n or visited[row][col] == True or board[row][col] != word[curChar]:
            return False

        # if the char match - move forward
        visited[row][col] = True

        up = self.backTrack(row - 1, col, m, n, visited, curChar + 1, board, word)
        down = self.backTrack(row + 1, col, m, n, visited, curChar + 1, board, word)
        left = self.backTrack(row, col - 1, m, n, visited, curChar + 1, board, word)
        right = self.backTrack(row, col + 1, m, n, visited, curChar + 1, board, word)

        visited[row][col] = False

        return up or down or left or right