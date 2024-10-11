# https://www.youtube.com/watch?v=faoVORjd-T8&ab_channel=NeetCodeIO

# Tc and Sc: O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        # Get the right most set bit
        '''
        The bit are differnt in certain position, from them get the right most bit where they are differnt
        '''
        right_most_set = (xor & (xor - 1)) ^ xor
        # print(right_most_set)

        # Bucket the number based on the bit value at the position
        a , b = 0 , 0
        for num in nums:
            if right_most_set & num == 0:
                a ^= num
            else:
                b ^= num
        
        return [a, b]
