'''

191. Number of 1 Bits
Easy

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

n = 00000000000000000000000000001011
s = Solution()
print(s.hammingWeight(n))