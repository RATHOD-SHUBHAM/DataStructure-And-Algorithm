class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                # we know for sure left to mid are in order
                if target >= nums[left] and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else: # nums[mid] < nums[right]
                # we know that mid to right are in order
                if target >= nums[mid] and target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            
        return -1