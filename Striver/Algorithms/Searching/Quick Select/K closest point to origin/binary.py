import math

class Solution:
    def swap(self, i, j, points):
        points[i], points[j] = points[j], points[i]


    def getDistance(self, point):
        x1 = 0
        y1 = 0

        x2 , y2 = point

        euclidian_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return euclidian_distance

    def binary_sort(self, points, left, right):
        # Consider mid to be our pivot val
        pivotIdx = left + (right - left) // 2
        pivotVal = self.getDistance(points[pivotIdx])

        # Place all the element smaller than this pivotVal to the left of it
        while left <= right:
            left_distance = self.getDistance(points[left])

            if left_distance >= pivotVal:
                self.swap(left, right, points)
                right -= 1
            else:
                left += 1


        # if left is same as pivot or greater than pivot then all the elements on left of pivot is smaller than pivot
        left_distance = self.getDistance(points[left])
        if left_distance < pivotVal:
            # Pivot point is on the left
            left += 1
            # all the element on left is smaller than this val
            return left
        else:
            return left

    def binary_quick_select(self, points, k):
        n = len(points)

        # Initial Hypothetical Pivot Index
        pivot_idx = n

        left = 0
        right = n - 1

        while pivot_idx != k: 
            # get the new pivot index
            new_pivot_idx = self.binary_sort(points, left, right)

            if new_pivot_idx < k:
                left = new_pivot_idx
            elif new_pivot_idx > k:
                right = new_pivot_idx - 1
            else:
                # new_pivot_idx == k
                break
            
            pivot_idx = new_pivot_idx
        
        return points[ : k]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.binary_quick_select(points, k)