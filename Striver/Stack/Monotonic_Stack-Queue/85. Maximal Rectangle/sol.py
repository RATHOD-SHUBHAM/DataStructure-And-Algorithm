# Tc: O(m*n) for prefix sum + O(n) Histogram stuff
# Sc: O(m*n) + O(n)

from typing import List
import math

class Solution:
    def PSEE(self, arr: List[int], n: int) -> List[int]:
        op = [-1] * n

        stack = []

        for i in range(n):
            cur_ele = arr[i]

            while stack and cur_ele <= arr[stack[-1]]:
                stack.pop()
            
            if not stack:
                op[i] = -1
            else:
                op[i] = stack[-1]
            
            stack.append(i)
        
        return op
    
    def NSEE(self, arr: List[int], n:int) -> List[int]:
        op = [-1] * n
        
        stack = []

        for i in reversed(range(n)):
            cur_ele = arr[i]

            while stack and cur_ele <= arr[stack[-1]]:
                stack.pop()
            
            if not stack:
                op[i] = n
            else:
                op[i] = stack[-1]
            
            stack.append(i)
        
        return op


    def histogramRectangle(self, arr: List[int], n:int) -> int:

        psee = self.PSEE(arr, n)
        # print(psee)
        nsee = self.NSEE(arr, n)
        # print(nsee)

        max_area_of_rectangle = -math.inf
        for i in range(n):
            length = arr[i]

            left_side_boundary = i - psee[i]
            right_side_boundary = nsee[i] - i

            width = left_side_boundary + right_side_boundary - 1

            area_of_rectangle = length * width

            max_area_of_rectangle = max(max_area_of_rectangle, area_of_rectangle)

        # print(max_area_of_rectangle)
        return max_area_of_rectangle



    def prefixSum(self, matrix: List[List[str]], m:int, n:int) -> List[List[int]]:

        prefix_sum = [[0 for _ in range(n)] for _ in range(m)]
        
        # First row will be the same
        for i in range(n):
            prefix_sum[0][i] = int(matrix[0][i])
        
        # print(prefix_sum)

        for i in range(1, m):
            for j in range(n):
                cur_num = int(matrix[i][j])

                if cur_num == 0:
                    prefix_sum[i][j] = 0
                else:
                    prefix_sum[i][j] = cur_num + prefix_sum[i-1][j]
        
        return prefix_sum

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        prefix_sum = self.prefixSum(matrix, m, n)
        # print(prefix_sum)

        max_rectangle_area = -math.inf
        for i in range(m):
            arr = prefix_sum[i]
            rectangle_area = self.histogramRectangle(arr, n)
            max_rectangle_area = max(max_rectangle_area , rectangle_area)

        return max_rectangle_area