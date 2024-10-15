# Storing a pre set value = ans.

class Solution:
    def getFloor(self, x, n,  arr):
        ans = -1
        
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
        
    def getCeil(self, x, n, arr):
        
        ans = n
        left = 0
        right = n - 1
        
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] >= x:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
                
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        arr.sort()
        
        n = len(arr)
        
        floor = self.getFloor(x, n, arr)
        # print(arr[floor])
        floor = arr[floor] if floor != -1 else -1
        
        
        ceil = self.getCeil(x, n, arr)
        # print(arr[ceil])
        ceil = arr[ceil] if ceil != n else -1
        
        return [floor, ceil]
        