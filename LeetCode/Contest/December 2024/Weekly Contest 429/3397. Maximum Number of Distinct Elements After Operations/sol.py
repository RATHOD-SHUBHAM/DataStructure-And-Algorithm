class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()

        count = 0

        # keep track of previously used value
        prev_max = -math.inf

        for i in range(n):
            # Range of value for current number
            lower_bound = nums[i] - k
            upper_bound = nums[i] + k

            if prev_max < lower_bound:
                prev_max = lower_bound
                count += 1
            elif lower_bound <= prev_max < upper_bound:
                prev_max += 1
                count += 1
            else:
                # all the value in this range is used, hence this is a duplicate
                continue
        
        return count

