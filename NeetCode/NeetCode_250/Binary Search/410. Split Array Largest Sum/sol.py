class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        ans = sum(nums) # if there is only 1 split then our largest sum is sum of all elements

        while left < right:
            # pick a sum for the split and test if this is the minimized split
            # assumption: this is the minimized split
            mid = left + (right - left) // 2

            # greedily check if the assumed split can satisfy the k split condition
            split = 1 # the first split is already in progress
            cur_sum = 0

            for num in nums:
                if cur_sum + num > mid:
                    cur_sum = num
                    split += 1
                else:
                    cur_sum += num
            

            # Now check if the split is satisfied and then adjust the assumed minimized split
            if split > k:
                # then we need to increase the assumed minimized sum
                left = mid + 1
            else:
                ans = mid
                right = mid
        
        return ans


# ========================================= Without using an extra variable to store the answer =========================================


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            # pick a sum for the split and test if this is the minimized split
            # assumption: this is the minimized split
            mid = left + (right - left) // 2

            # greedily check if the assumed split can satisfy the k split condition
            split = 1 # the first split is already in progress
            cur_sum = 0

            for num in nums:
                if cur_sum + num > mid:
                    cur_sum = num
                    split += 1
                else:
                    cur_sum += num
            

            # Now check if the split is satisfied and then adjust the assumed minimized split
            if split > k:
                # then we need to increase the assumed minimized sum
                left = mid + 1
            else:
                right = mid
        
        return right