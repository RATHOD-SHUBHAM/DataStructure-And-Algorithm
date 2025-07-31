# Prereq - LC: 84, Largest Rectangle in Histogram

class Solution:

    def PSEE(self, arr, n):
        op = [-1] * n
        stack = []

        for i in range(n):
            cur_ele = arr[i]

            # Look for previous smaller element
            while stack and cur_ele <= arr[stack[-1]]:
                stack.pop()
            
            if not stack:
                op[i] = -1
            else:
                op[i] = stack[-1]
            

            stack.append(i)
        
        return op
    
    def NSEE(self, arr, n):
        op = [n] * n

        stack = []

        for i in reversed(range(n)):
            cur_ele = arr[i]

            # look for next smaller element
            while stack and cur_ele <= arr[stack[-1]]:
                stack.pop()
            
            if not stack:
                op[i] = n
            else:
                op[i] = stack[-1]
            

            stack.append(i)
        
        return op
    
    def calculateBuilding(self, psee, nsee, heights, n):

        area = [None] * n

        for i in range(n):
            length = heights[i]

            left_boudary = i - psee[i]
            right_boundary = nsee[i] - i

            # Reduce one as both include current building also
            width = left_boudary + right_boundary - 1

            area[i] = length * width
        
        return area

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # Get left and right smaller buildings
        psee = self.PSEE(heights, n)
        # print(psee)
        nsee = self.NSEE(heights, n)
        # print(nsee)

        # Calculate the area individual building
        area = self.calculateBuilding(psee, nsee, heights, n)
        # print(area)

        return max(area)


    def prefixSum(self, matrix, m, n):
        
        prefix_sum = [[0 for _ in range(n)]for _ in range(m)]

        for j in range(n):
            prefix_sum[0][j] = int(matrix[0][j])

        for i in range(1, m):
            for j in range(n):
                if int(matrix[i][j]) == 0:
                    continue
                
                prefix_sum[i][j] = int(matrix[i][j]) + prefix_sum[i-1][j]
        
        return prefix_sum

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        prefix_sum = self.prefixSum(matrix, m, n)

        max_area = -math.inf
        for i in range(m):
            heights = prefix_sum[i]

            cur_area = self.largestRectangleArea(heights)

            max_area = max(max_area, cur_area)

        return max_area

