class Solution:
    # Floor Function - Upper Bound
    def getFloor(self, x, n,  arr):
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
        
    # Ceil Function - Lower Bound
    def getCeil(self, x, n, arr):
        
        left = 0
        right = n - 1
        
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if x == arr[mid]:
                return mid
            elif x < arr[mid]:
                if mid - 1 == -1:
                    return 0
                elif arr[mid - 1] < x:
                    return mid
                else:
                    right = mid - 1
            else:
                if mid + 1 == n:
                    # return n
                    return -1
                elif x < arr[mid + 1]:
                    return mid + 1
                else:
                    left = mid + 1

    # Main Code           
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        arr.sort()
        
        n = len(arr)
        
        floor = self.getFloor(x, n, arr)
        # print(arr[floor])
        floor = arr[floor] if floor != -1 else -1
        
        
        ceil = self.getCeil(x, n, arr)
        # print(arr[ceil])
        ceil = arr[ceil] if ceil != -1 else -1
        
        return [floor, ceil]


# ---------------- Preset ----------------

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
        