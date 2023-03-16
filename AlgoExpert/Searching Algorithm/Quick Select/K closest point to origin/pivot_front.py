'''
Quick Select

Idea is:
    When we place the Pivot at right position -- 
        1] All the elements to left of pivot is smaller than pivot.
            &
        2] All the elements to the right of pivot is greater than pivot.

Return everything that is on left -- and this will be our closest value
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:    
        pos = k - 1
        return self.quickSelect(0, len(points) - 1, points, pos)
    
    def quickSelect(self,start,end,array,pos):
        
        while start <= end:
            pivot = start
            left = start + 1
            right = end
            
            while left <= right:
                
                if self.dist(array[left]) > self.dist(array[pivot]) and self.dist(array[right]) < self.dist(array[pivot]):
                    self.swap(array,left,right)
                    
                if self.dist(array[left]) <= self.dist(array[pivot]):
                    left += 1
                    
                if self.dist(array[right]) >= self.dist(array[pivot]):
                    right -= 1
                    
            self.swap(array,pivot,right)
            
            if right == pos:
                return(array[:pos+1])
            elif pos < right:
                end = right - 1
                self.quickSelect(start,end,array,pos)
            else:
                start = right + 1
                self.quickSelect(start,end,array,pos)
                
    def dist(self,array):
        return array[0] ** 2 + array[1] ** 2
    
    def swap(self,array,left,right):
        array[left],array[right] = array[right],array[left]