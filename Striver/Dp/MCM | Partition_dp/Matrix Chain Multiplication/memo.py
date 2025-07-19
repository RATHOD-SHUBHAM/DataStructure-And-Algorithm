import math

class Solution:
    def matrixMultiplication(self, arr):
        # code here
        
        n = len(arr)
        
        # i represents the starting matrix index
        # j represents the ending matrix index
        i = 1 
        j = n-1
        
        memo= {}
        
        return self.recursion(i, j, memo, n, arr)
    
    def recursion(self, i, j, memo, n, arr):
        """
        Matrix at index i has dimensions arr[i-1] x arr[i]
        Matrix at index j has dimensions arr[j-1] x arr[j]
        """
        
        # base case
        if i == j:
            # single matrix -> no operation
            return 0
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        min_operations = math.inf
        
        # Try all possible partition points k between i and j-1
        for k in range(i, j):
            """
            k represents the partition point where we split the matrix chain.
            
            We split the matrices into two groups:
            - Left group: matrices from i to k 
            - Right group: matrices from k+1 to j
            
            Example with arr = [10, 20, 30, 40, 50]:
            If i=1, j=4, k=2:
            - Left group: M1 (matrices 1 to 2) -> results in matrix of size arr[0] x arr[2] = 10x30
            - Right group: M2,M3 (matrices 3 to 4) -> results in matrix of size arr[2] x arr[4] = 30x50
            - Final multiplication: (10x30) * (30x50) = 10*30*50 operations
            """
            # Calculate operations needed for left subproblem (matrices i to k)
            left_operations = self.recursion(i, k, memo, n, arr)
            
            # Calculate operations needed for right subproblem (matrices k+1 to j)  
            right_operations = self.recursion(k + 1, j, memo, n, arr)
            
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
        
        memo[(i,j)] = min_operations
        
        return min_operations
            