'''

51. N-Queens
Hard


The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9





'''





'''

Time Complexity = O(n!)
Space Complexity = O(n)
Step:
i] Create a board.
Finalboard = [[]*n for _ in range(n)] this will create a list of list [[],[],[],[]] # when n = 4

ii] Create a list to keep track of --> In which column the queen is placed at a particular row.

# each index is considered to be a row
        queenTracker = [0] * n # keep track of col in which queen is placed
iii] Call the Validate function -> to check if all the queens are placed in correct position.

Queens are placed in correct position --- when we have completed our recursice call. ie., after placing queen at right column in each and every row. We will reach a condition, where we have placed our queen at right column in every row.
at this time we would have gone through every row :
if row == n:
            self.board(queenTracker,Finalboard,n,ans)
            return 1
# this will form the base case and we add queen at to the board. and we return 1 stating that we have completed placing all queen in their right position -- (this is just like an acknowlegment)
iv] validate function will call 'is valid position function' to check if the queen is not being placed in the same col and in the same diagonal as the previous queens.

v] place the "." and "q" in the board -- once we know position of all the queen in their right place. ie., when we are about to return 1 or when we have traversed every row in the board.

'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # creating a board
        ans = []
        Finalboard = [[]*n for _ in range(n)]
        
        # each index is considered to be a row
        queenTracker = [0] * n # keep track of col in which queen is placed
        self.validate(0 , n , queenTracker,Finalboard,ans)
        
        return ans
    
    def validate(self,row,n,queenTracker,Finalboard,ans):
        # base case: when i move out of the last row. I have finished placing every queen in right position.
        if row == n:
            self.board(queenTracker,Finalboard,n,ans)
            return 1
        
        validPositionCount = 0
        
        for col in range(n):
            if self.isValidPosition(row,col,queenTracker):
                queenTracker[row] = col
                validPositionCount +=  self.validate(row+1,n,queenTracker,Finalboard,ans)
                
        return validPositionCount
    
    # check if there are no queen in particular col and in diagonal col
    def isValidPosition(self,row,col,queenTracker):
        for previousRow in range(row):
            colToCheck = queenTracker[previousRow]
            
            # check if they are in same col
            sameCol = False
            if col == colToCheck:
                sameCol = True
            '''
            This can be written as
            sameCol = (col == colToCheck)
            '''

            # check diagonal => abs(x2 - x1) = abd(y2 - y1)
            sameDiagonal = False
            if abs(col - colToCheck) == abs(row - previousRow):
                sameDiagonal = True
            
            '''
            This can be written as
            sameDiagonal = abs(col - colToCheck) == abs(row - previousRow)
            '''

            if sameCol or sameDiagonal:
                return False
            
        return True
    
    
    def board(self,queenTracker,Finalboard,n,ans):
        for row in range(len(queenTracker)):
            Finalboard[row] = '.'*(queenTracker[row]) + 'Q' + '.'*(n-(queenTracker[row]) -1 )
        copy = Finalboard[:]
        ans.append(copy)
        
        return ans
		
# So basically we traverse the board, check if the queens are in right position. If yes then place the queen on baord. Else go back change the position of previous queen. check again and repeat until we get the right position.