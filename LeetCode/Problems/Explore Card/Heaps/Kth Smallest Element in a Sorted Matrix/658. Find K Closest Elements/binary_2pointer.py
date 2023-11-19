# Time: O(log n + k)
# space = O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # time: log n
        # first find the x in list of array
        left = 0
        right = len(arr) - 1
        
        curClosest = arr[0]
        idx = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # if x is present in the arr
            if arr[mid] == x:
                idx = mid
                curClosest = arr[mid]
                break
            
            # if x is not present in array
            # use the condition to find closes ele
            if ( abs(arr[mid] - x) < abs(curClosest - x) ) or ( (abs(arr[mid] - x) == abs(curClosest - x) and (arr[mid] < curClosest) ) ):
                idx = mid
                curClosest = arr[mid]
                
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # Time = O(k)
        # here i have found curClosest value and its idx to x
        left = right = idx # assigning left and right pointer to mid value
        
        while right - left < k - 1:
            if left == 0:
                right += 1
            
            elif right == len(arr) - 1:
                left -= 1
            
            # check weather to move right or left pointer
            elif (abs(arr[left - 1] - x) <= abs(arr[right + 1] - x)):
                left -= 1
            else:
                right += 1
                
        return arr[left : right + 1]
                
                