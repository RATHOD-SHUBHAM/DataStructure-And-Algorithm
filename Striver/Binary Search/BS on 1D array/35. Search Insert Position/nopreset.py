# Without preset value
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                if mid + 1 == n:
                    return n
                elif target < nums[mid + 1]:
                    return mid + 1
                else:
                    left = mid + 1
            
            else: # nums[mid] > target
                if mid - 1 == -1:
                    return 0
                elif nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1