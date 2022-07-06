'''
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
Medium

2303

321

Add to List

Share
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

 

Example 1:


Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:


Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
 

Constraints:

2 <= h, w <= 109
1 <= horizontalCuts.length <= min(h - 1, 105)
1 <= verticalCuts.length <= min(w - 1, 105)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
All the elements in horizontalCuts are distinct.
All the elements in verticalCuts are distinct.

'''

# Find the maximum height and Maximum width after the cut is made

# time = O(nlog(n) + mlog(m))
# space = O(1)


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        # sort the cuts to have them in proper order
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # Find the max height
        # taking care of edges
        max_height = max(horizontalCuts[0] , h - horizontalCuts[-1])
        
        for i in range(1, len(horizontalCuts)):
            current_cut_height = horizontalCuts[i] - horizontalCuts[i-1]
            max_height = max(max_height , current_cut_height)
            
        # Find the max_width
        # taking care of edges
        max_width = max(verticalCuts[0] , w - verticalCuts[-1])
        
        for i in range(1 , len(verticalCuts)):
            current_cut_width = verticalCuts[i] - verticalCuts[i-1]
            max_width = max(max_width , current_cut_width)
            
        max_area_of_cake_piece = max_height * max_width
        
        return max_area_of_cake_piece % ((10**9) + 7)