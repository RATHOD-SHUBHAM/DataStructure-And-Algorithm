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