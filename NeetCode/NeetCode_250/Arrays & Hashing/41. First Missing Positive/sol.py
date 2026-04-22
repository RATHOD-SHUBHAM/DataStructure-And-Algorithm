# Note that positive integers are greater than zero.

'''
For an array of length n, if the array does not contain all of the integers in the range 1 to n+1, the smallest missing positive integer is the first integer missing from that range.

eg: range [1, n+1]
[1,2,3] -> range [1,4] > missing 4
[2,3,4] -> range [1,4] > missing 1
[7,8,9,11,12] -> range [1,6] > missing 1
'''

# Tc and Sc :O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # max_range = (10 ** 5) + 1

        max_range = n+1

        num_set = set(nums)

        for x in range(1, max_range):
            if x not in num_set:
                return x
            