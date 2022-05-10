class Solution:
    def kClosest(self, points, k):
        return self.quickSelect(points, k)

    def quickSelect(self, points, k):
        left = 0
        right = len(points) - 1

        #check if the k value is same as number of elements in pivot
        '''
        if len(pivot) == k:
            return pivot

            or
        '''

        pivot_index = len(points)

        while pivot_index != k:
            pivot_index = self.partition(points,left,right) # divide the array by placing the pivot at right position

            # if my k < pivot then I should sort left array
            if k > pivot_index:
                left = pivot_index  
            elif k < pivot_index:
                right = pivot_index - 1

        return(points[:k])


    def partition(self,points,left,right):
        # find the pivot
        pivot = self.pivot(left,right)
        pivotVal = points[pivot]

        while left < right:
            # start putting the elements greater than pivot to right of pivot
            if points[left] >= pivotVal:
                self.swap(points,left,right)
                right -= 1 # the greater array is on right of pivot so decrese the pointer
            else:
                left += 1


        # if my left is same as pivot or greater than pivot then all the elements on left of pivot is sorted
        if points[left] < pivotVal:
            left += 1
            return left
        else: # points[left] >= points[pivot] # if my left is same as pivot or greater than pivot then all the elements on left of pivot is sorted
            return left


    def pivot(self,left,right):
        mid = left + (right - left)//2
        return mid
        

    def swap(self,array,left,right):
        array[left], array[right] = array[right], array[left]



if __name__ == '__main__':
    points = [18,26,20,10,8]
    k = 2
    print("min k value: ",Solution().kClosest(points, k))