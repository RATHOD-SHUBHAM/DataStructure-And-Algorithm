# --------------------- Brute Force ---------------------

# Push the scale
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for num in arr:
            if num > k:
                return k
            else:
                k += 1
        return k
    
# --------------------- Set Brute Force ---------------------

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        set_arr = set(arr)

        n = len(arr)

        cur_missing = k

        for i in range(n):
            if cur_missing < arr[i]:
                return cur_missing
            
            # if any number is present - push the missing number by one
            if arr[i] in set_arr:
                cur_missing += 1
        
        return cur_missing

# --------------------- Better ---------------------

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)

        # Total no of missing numbers present at that value
        no_missing_value = [0] * n
        for i in range(n):
            no_missing_value[i] = arr[i] - (i + 1)
        # print(no_missing_value)

        # Find the number in between which missing number is present
        # Eg k = 5, is between 3 and 6
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if no_missing_value[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
            
        # based on the formula for finding missing number
        return k + left

# --------------------- Optimal ---------------------

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)

        # Find the number in between which missing number is present
        # Eg k = 5, is between 3 and 6
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Finding total # of missing number at the current value
            no_missing_value = arr[mid] - (mid + 1)

            if no_missing_value < k:
                left = mid + 1
            else:
                right = mid - 1
            
        # based on the formula for finding missing number
        return k + left