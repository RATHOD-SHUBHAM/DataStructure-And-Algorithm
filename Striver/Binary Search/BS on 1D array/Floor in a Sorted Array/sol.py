class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,n,x):
        #Your code here
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if x == arr[mid]:
                return mid
            elif x < arr[mid]:
                if mid - 1 == -1:
                    return -1
                elif x > arr[mid - 1]:
                    return mid - 1
                else:
                    right = mid - 1
            else:
                if mid + 1 == n:
                    return mid
                elif x < arr[mid + 1]:
                    return mid
                else:
                    left = mid + 1
        
        return left