'''

118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30


'''
# Tc: O(numRows^2)
# SC: O(1) #  the input and output generally do not count towards the space complexity.



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        
        for _ in range(numRows - 1):
            temp = [0] + triangle[-1] + [0] # appending 0 front and back
            
            row = []
            
            for i in range(len(temp) - 1):
                row.append(temp[i] + temp[i+1])
                
            triangle.append(row)
            
        return triangle