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
            