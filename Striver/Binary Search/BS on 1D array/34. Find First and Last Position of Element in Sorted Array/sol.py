class Solution:
    def get_floor(self, nums, target, n):
        left = 0
        right = n - 1

        ans = 0


        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                ans = mid
                left = mid + 1
            else: # nums[mid] > target
                right = mid - 1
        
        return ans

    def get_ceil(self, nums, target, n):
        
        ans = n

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1 , -1]
        
        n = len(nums)
        ans = [-1, -1]

        end = self.get_floor(nums, target, n)
        if end >= 0 and nums[end] == target:
            ans[1] = end
        
        start = self.get_ceil(nums, target, n)
        if start < n and nums[start] == target:
            ans[0] = start
        
        return ans