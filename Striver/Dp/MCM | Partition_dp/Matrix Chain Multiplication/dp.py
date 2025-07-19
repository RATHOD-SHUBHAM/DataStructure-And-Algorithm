import math

class Solution:
    def matrixMultiplication(self, arr):
        # code here
        
        n = len(arr)
        
        dp = [[math.inf for _ in range(n)]for _ in range(n)]
        
        # Base case: Single matrices require 0 operations
        for i in range(n):
            # i == j
            dp[i][i] = 0
        
        for i in reversed(range(1, n)): # in recursion 1-n, so here we reverse it
            for j in range(i+1, n): # in recursion n-1, 9, here we reverse it but, j will always be to the right of i
                
                min_operations = math.inf
                for k in range(i, j):
                    # Calculate operations needed for left subproblem (matrices i to k)
                    left_operations = dp[i][k]
                    
                    # Calculate operations needed for right subproblem (matrices k+1 to j)  
                    right_operations = dp[k+1][j]
                    
                    # Total operations for both subproblems
                    no_of_subset_operations = left_operations + right_operations
                    
                    
                    # Operations needed to multiply the two resulting matrices
                    # Left result has dimensions: arr[i-1] x arr[k]
                    # Right result has dimensions: arr[k] x arr[j]  
                    # Multiplication cost: arr[i-1] * arr[k] * arr[j]
                    no_of_operations = arr[i-1] * arr[k] * arr[j]
                    
                    # Total operations = subproblem operations + final multiplication
                    total_no_of_operations = no_of_subset_operations + no_of_operations
                    
                    min_operations = min(min_operations, total_no_of_operations)
                
                dp[i][j] = min_operations
        
        # Return minimum operations to multiply all matrices (from 1 to n-1)
        return dp[1][n-1]
            