class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)

        smallest_divisor = -1

        left = 1
        right = max(nums)

        while left <= right:
            mid = left + (right - left) // 2

            cur_sum = 0
            for num in nums:
                cur_sum += math.ceil(num/mid)
            
            
            if cur_sum <= threshold:
                '''Moving left will increase the cur_sum because the numbers get divided by smaller number'''
                smallest_divisor = mid
                right = mid - 1
            else:
                left = mid + 1
        

        return smallest_divisor