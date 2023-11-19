# Time = O(n)
# Space = O(1)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quickSelect(points,k)
    
    
    def quickSelect(self,array,k):
        left = 0
        right = len(array) - 1
        
        '''
        if len(array) == k:
        return array
        
        or 
        
        pivot_index = len(array)
        '''
        # check if k value covers the entire array
        pivot_index = len(array)
        
        while pivot_index != k:
            # find out the pivot element -- place the pivot element in its correct place and if k value is met all the element on left of pivot is nearest point to origin
            pivot_index = self.partition(array,left,right)
            # print("pivot_index", pivot_index)
            
            
            # check if I have to move left or right to pivot
            if k < pivot_index:
                right = pivot_index
            elif k > pivot_index:
                left = pivot_index # every element on left of pivot is smaller - so we got to incluse pivot as well
                
        return(array[:pivot_index])
    
    
    def partition(self,array,left,right):
        # find pivot
        pivot = self.pivot(array,left,right)
        # print("pivot",pivot)
        
        # find the distance of pivot from center
        pivotDist = self.euclid(pivot)
        # print("pivotDist", pivotDist)
        
        
        while left < right:
            # put all the value greater than pivot to right of it
            if self.euclid(array[left]) >= pivotDist:
                self.swap(array,left,right)
                # print("array after swap: ",array)
                right -= 1
            else:
                left += 1
            
        # move upto point of euclidian distance
        if self.euclid(array[left]) < pivotDist:
            left += 1 # returning the pivot value
        
        return left
        
    def pivot(self,array,left,right):
        # mid = left + (right - left)//2
        # return array[mid] 
        return array[left + (right - left)//2]
    
    def euclid(self,array):
        # dist = array[0] ** 2 + array[1] ** 2
        # return dist 
        return  array[0] ** 2 + array[1] ** 2
    
    def swap(self, array,left,right):
        array[left], array[right] = array[right], array[left]