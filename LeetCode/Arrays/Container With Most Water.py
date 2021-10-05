"""

11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

"""
from typing import List


class Solution():
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxArea = 0


        while left <= right:
            print("left is : ",height[left])
            print("right is : ",height[right])
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            # if right is small or if two elements are same
            else:
                area = height[right] * (right - left)
                right -= 1
            maxArea = max(maxArea,area)
            # print(maxArea)
        return maxArea


def main():
    height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    myfunc = s.maxArea(height)
    print(myfunc)


if __name__ == '__main__':
    main()
