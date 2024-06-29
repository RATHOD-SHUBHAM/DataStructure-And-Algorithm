'''
    Note:
        Wont work for negative number.

        Hence Wrong answer
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        left = 0

        subarray_count = 0

        while left < n:

            right = left
            cur_sum = 0

            while right < n:
                cur_sum +=  nums[right]

                if cur_sum == k:
                    subarray_count += 1
                    break
                elif cur_sum > k:
                    break
                else:
                    right += 1

            left += 1 
        
        print(subarray_count)
        return subarray_count