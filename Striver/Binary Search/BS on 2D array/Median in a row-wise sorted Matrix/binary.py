import math

class Solution:
    def binarySearch(self, arr, cur_ele, n):
        '''Find first occurance of number greater than cur_ele'''
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] <= cur_ele:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
            
            
    def lessThanEqual(self, matrix, cur_ele, m, n):
        # Count of numbers less than or equal to cur_num
        count_of_number = 0
        
        for i in range(m):
            arr = matrix[i]
            count_of_number += self.binarySearch(arr, cur_ele, n)
        
        return count_of_number
        
    def median(self, matrix, R, C):
        #code here
        V = R * C
        
        # Median 
        threshold = math.ceil(V / 2) # the count where we can find the median
    # 	print(threshold)
        
        # Get the low and high value
        """Since the matrix is row wise sorted
        Min number will be found in first column
        Max number will be found in last column
        """
        col = 0
        low = math.inf
        for row in range(R):
            low = min(matrix[row][col], low)
            
        high = -math.inf
        col = C - 1
        for row in range(R):
            high = max(matrix[row][col], high)
        
        median_number = -1
        
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # get the count of numbers less than or equal to cur_num
            count_of_number = self.lessThanEqual(matrix, mid, R, C)
            
            if count_of_number < threshold:
                low = mid + 1
            else:
                median_number = mid
                high = mid - 1
                
        return median_number