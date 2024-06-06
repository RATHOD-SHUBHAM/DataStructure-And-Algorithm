# Tc: TLE | Sc: O(1)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(n):
            if i == n - 1:
                arr[i] = -1
                continue

            max_value = max(arr[i+1 : ])
            arr[i] = max_value
        
        return arr
    
# ------------ Reverse the array and find the greatest ---------------

# Tc: O(n) | Sc: O(1)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        greatest = arr[-1]

        arr[-1] = -1

        for i in reversed(range(n - 1)):
            cur_val = arr[i] # store the current value

            arr[i] = greatest # Update the value at current position

            # Update the gratest value
            if cur_val > greatest:
                greatest = cur_val
        
        # print(arr)
        return arr
            