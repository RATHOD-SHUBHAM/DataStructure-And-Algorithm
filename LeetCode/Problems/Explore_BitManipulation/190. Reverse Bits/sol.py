'''
Summary:
Take the left most bit from n, append it to right most bit of result.

Steps to reverse the bits:
1. AND: (n & 1) , will give us the left most bit value.
2. Right shift: Shift n to the right by one position

3. Left Shift: move (n & 1) to the right most postion of result
4. OR: perform an OR of (n & 1) and result bit
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 # this will be a 32 bit binary

        for i in range(32):
            # step 1:
            bit_val = n & 1
            # step 2:
            n = n >> 1

            # step 3:
            bit_val = bit_val << (31 - i)
            # step 4:
            result = result | bit_val

        return result        