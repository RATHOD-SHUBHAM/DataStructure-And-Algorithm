# Tc: O(n) and Sc: O(1)
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        hamming_dist = 0
        
        # The answer for the given input will fit in a 32-bit integer.
        # go over constant 32 bit
        for _ in range(32):
            # get the number of ones in the last bit
            count_ones = 0
                
            for i in range(n):
                # check if there is one in last bit
                # if num & 1:
                count_ones += nums[i] & 1
                
                # move the bit
                nums[i]  >>= 1
                
            # get the number of zero
            count_zero = n - count_ones
            
            # the difference between all the bit
            # 0 , 1, 1 = diff = (01) (01) = 2 or = 1 zero 2 one = 1 * 2 = 2
            hamming_dist += (count_zero * count_ones)
            
        return hamming_dist
    
       