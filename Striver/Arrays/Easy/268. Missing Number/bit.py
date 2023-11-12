'''
    eg : nums = [3, 0 , 1]

    n = 3

    XOR_N =     0 , 1, 2, 3
    XOR_NUMS =  0 , 1, _, 3

    XOR_N ^ XOR_NUMS = 0, 0, 2 , 0

    Becasue XOR of same number is 0 and differnet number is number itself
'''


# Tc: O(n) | Sc: O(1)

# Gauss Formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        xor_n = 0
        for i in range(n+1):
            xor_n = xor_n ^ i
        


        xor_nums = 0
        for i in nums:
            xor_nums = xor_nums ^ i


        return xor_n ^ xor_nums