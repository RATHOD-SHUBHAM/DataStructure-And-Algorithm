'''
    a + k = x

    a can also be written as = x - k

    (x - k) + k = x


    x - k is the prefix sum

    if i can find out how many x - k are available , then we know that for sure that many K value will be available.
'''


# prefix sum
# Tc and Sc = O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dic = {0 : 1} # because if entire array forms a subarray then we need to have a count of 0
        
        cur_sum = 0

        subarray_count = 0

        for i in range(n):
            cur_sum += nums[i]

            prefix_sum = cur_sum - k

            # Check if there exist a subarray  after the prefix point
            if prefix_sum in dic:
                subarray_count += dic[prefix_sum]
            
            if cur_sum in dic:
                dic[cur_sum] += 1
            else:
                dic[cur_sum] = 1
        
        return subarray_count