class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quickSelect(points , k)
    
    def quickSelect(self, array , k):
        left = 0
        right = len(array) - 1
        
        pivot_idx = len(array)
        
        while k != pivot_idx:
            
            pivot_idx = self.position(left, right, array)
            
            if pivot_idx < k:
                left = pivot_idx
            elif pivot_idx > k:
                right = pivot_idx
        
        return array[ : pivot_idx]
    
    def position(self, left , right , array):
        pivot_ele = self.pivot(left , right, array)
        
        pivot_dist = self.euclid(pivot_ele)
        
        while left < right:
            if self.euclid(array[left]) >= pivot_dist:
                self.swap(left, right, array)
                right -= 1
            else:
                left += 1
                
        while self.euclid(array[left]) < pivot_dist:
            left += 1
            
        return left
    
    def pivot(self, left, right, array):
        mid = left + (right - left) // 2
        return array[mid]
    
    def euclid(self, arr):
        dist = arr[0] ** 2 + arr[1] ** 2
        return dist
    
    def swap(self, i , j , array):
        array[i] , array[j] = array[j] , array[i]