# brute force
# Tc: O(n^3) | Sc: O(1)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        max_area = -math.inf

        for i in range(n):
            for j in range(i, n):
                
                min_height = heights[i] # keeps track of smallest building
                for k in range(i, j+1):
                    min_height = min(min_height, heights[k])
                
                # length = the distance between i and j, breadth = minimum height building
                length = j - i + 1
                cur_area = length * min_height

                max_area = max(max_area , cur_area)
        
        return max_area
        
# ----------------------------------- Better Approach -----------------------------------

# Tc: O(n^2) | Sc: O(1)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        max_area = -math.inf

        for i in range(n):
            min_height = heights[i] # keeps track of smallest building

            for j in range(i, n):
                # length = the distance between i and j, breadth = minimum height building
                min_height = min(min_height, heights[j])
                length = j - i + 1
                
                cur_area = length * min_height

                max_area = max(max_area , cur_area)
        
        return max_area
    

# ----------------------------------- Optimal Approach -----------------------------------
# Tc and Sc: O(n)

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
