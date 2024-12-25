import math

class Solution:
    def swap(self, i, j, points):
        points[i] , points[j] = points[j], points[i]

    def getDistance(self, points):
        x1 = 0
        y1 = 0

        x2 , y2 = points

        euclidian_dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        return euclidian_dist
    
    def quickSelect(self, points, k , startIdx, endIdx):
        if startIdx >= endIdx:
            return points[ : k]
        
        pivotIdx = startIdx
        left = startIdx + 1
        right = endIdx

        while left <= right:
            pivotIdx_dist = self.getDistance(points[pivotIdx])
            # print(pivotIdx_dist)
            left_dist = self.getDistance(points[left])
            # print(left_dist)
            right_dist = self.getDistance(points[right])
            # print(right_dist)

            if left_dist > pivotIdx_dist and right_dist < pivotIdx_dist:
                self.swap(left, right, points)
            
            if left_dist <= pivotIdx_dist:
                left += 1
            
            if pivotIdx_dist <= right_dist:
                right -= 1
        
        self.swap(pivotIdx, right, points)
        # print(points, right)

        if right == k:
            return points[ : k]
        elif right < k:
            return self.quickSelect(points, k, right + 1, endIdx)
        else:
            return self.quickSelect(points, k, startIdx, right - 1)


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Quick Select
        n = len(points)

        startIdx = 0
        endIdx = n - 1

        return self.quickSelect(points, k, startIdx, endIdx)