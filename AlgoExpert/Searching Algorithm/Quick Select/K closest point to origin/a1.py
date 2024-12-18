# --------------------- Brute Force  ---------------------

import math

class Solution:
    def getDistance(self, points):
        x1 = 0
        y1 = 0

        distance_array = []

        for i in range(len(points)):
            x2 , y2 = points[i]

            cur_dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            distance_array.append([cur_dist, i])
        
        return distance_array


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_array = self.getDistance(points)

        # Sort the array
        distance_array.sort()
        print(distance_array)

        op = []
        for i in range(k):
            idx = distance_array[i][1]
            op.append(points[idx])

        return op
    

# --------------------- Quick Select  ---------------------

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
    

# --------------------- Binary Search + Quick Select  ---------------------

class Solution:
    def kClosest(self, points, k):
        return self.quickSelect(points, k)

    def quickSelect(self, points, k):
        n = len(points)

        left = 0
        right = n - 1

        pivot_index = n

        while pivot_index != k:
            # Binray Search
            pivot_index = self.partition(points,left,right) # divide the array by placing the pivot at right position

            # if my k < pivot then I should sort left array
            if k > pivot_index:
                left = pivot_index  
            elif k < pivot_index:
                right = pivot_index - 1

        return(points[:k])


    def partition(self,points,left,right):
        '''Binary Search'''
        
        # find the pivot
        pivot = left + (right - left) // 2 # Mid
        pivotVal = self.getDistance(points[pivot])
        # print(pivotVal)

        '''Sort the Points'''
        while left < right:
            # start putting the elements greater than pivot to right of pivot
            if self.getDistance(points[left]) >= pivotVal:
                # swap elements to make sure that all points closer than the pivot are to the left
                self.swap(points,left,right)
                right -= 1 # the greater array is on right of pivot so decrese the pointer
            else:
                left += 1


        # print(points)
        
        # if my left is same as pivot or greater than pivot then all the elements on left of pivot is sorted
        if self.getDistance(points[left]) < pivotVal:
            left += 1 # pivot value is on left
            # print(left)
            return left
        else: # points[left] >= points[pivot] # if my left is same as pivot or greater than pivot then all the elements on left of pivot is sorted
            return left
    

    def getDistance(self, points):
        x1 = 0
        y1 = 0

        x2 , y2 = points

        euclidian_dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        return euclidian_dist
        

    def swap(self,array,left,right):
        array[left], array[right] = array[right], array[left]