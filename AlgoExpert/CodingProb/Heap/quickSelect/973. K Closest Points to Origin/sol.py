# time = O(n)
# space = O(1)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quickSelect(points , k)
    
    def quickSelect(self, array , k):
        left = 0
        right = len(array) - 1
        
        pivot_idx = len(array)
        
        while pivot_idx != k:
            pivot_idx = self.partition(array, left, right)
            
            if pivot_idx < k:
                left = pivot_idx
            elif pivot_idx > k:
                right = pivot_idx
                
        return array[ : pivot_idx]
    
    def partition(self, array, left, right):
        pivot_ele = self.pivot(array,left,right)
        
        pivot_dist = self.euclid(pivot_ele)
        
        while left < right:
            if self.euclid(array[left]) >= pivot_dist:
                self.swap(left , right , array)
                right -= 1
            else:
                left += 1
                
        while self.euclid(array[left]) < pivot_dist:
            left += 1
            
        return left
    
    
    def pivot(self, array, left, right):
        mid = left + (right - left) // 2
        return array[mid]
    
    def euclid(self, array):
        dist = array[0] ** 2 + array[1] ** 2
        return dist
    
    def swap(self, i , j , array):
        array[i] , array[j] = array[j] , array[i]