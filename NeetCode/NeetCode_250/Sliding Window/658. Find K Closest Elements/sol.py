class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # The approach: shrink a window from the outside in
        left = 0
        right = len(arr) - 1

        # Start with the entire array as your window, repeatedly shrink from whichever side is "worse" until exactly k elements remain.
        while (right - left) + 1 > k:
            # If left side different is farther than right side - shrink from left
            if abs(x - arr[left]) > abs(arr[right] - x):
                left += 1
            # If right side different is farther than left side or both are same - shrink from right: prefer the SMALLER value (a < b when |a-x| == |b-x|)
            elif abs(arr[right] - x) >= abs(x - arr[left]):
                right -= 1
        
        return arr[left : right + 1]

# ===================================================================================

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while (right - left) + 1 > k:
            # if left side is much farther
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
        
        return arr[left : right + 1]