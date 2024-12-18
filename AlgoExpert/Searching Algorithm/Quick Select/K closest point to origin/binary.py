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