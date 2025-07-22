"""
✅ Functions Overview
    You have broken the solution into:

    PSEE – Previous Smaller Element's Index

    NSEE – Next Smaller Element's Index

    calculateBuilding – Computes area for each bar

    largestRectangleArea – Main driver

⏱️ Time Complexity
    Let n be the number of elements in heights.

    PSEE and NSEE:

        Each index is pushed and popped from the stack at most once.

        So both PSEE and NSEE run in O(n) time.

    calculateBuilding:

        A single loop over n elements → O(n).

    largestRectangleArea:

        Just combines the above and calls max(area) which is also O(n).

🔁 Total Time Complexity: O(n)

    🧠 Space Complexity
        **PSEE, NSEE, area, and stack**: Each uses an array/list of size n`.

        So you use around 4 auxiliary arrays of size n.

    📦 Total Space Complexity: O(n)

✅ Final Answer:
    Time Complexity: O(n)

    Space Complexity: O(n)

"""

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


