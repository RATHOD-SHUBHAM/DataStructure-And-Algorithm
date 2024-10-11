# Tc: O(n) | Sc: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        # print(counter)

        for val, count in counter.items():
            if count != 3:
                return val
            

# -------------------- Bit --------------------
'''
we know that the maximum value of result is 2^31−1. 
So, if result turns out to be more than this, it means that the leftmost set bit is a sign bit. 
So, we need to convert it to 2's complement. 
We can do this by subtracting 2^32 from result
'''

# Tc: O(N * 32) | Sc: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for bit_position in reversed(range(32)):
            count = 0 # Count no of 1s

            for i in range(n):
                cur_num = nums[i]
                # Check if kth bit is set 
                kth_bit = cur_num & (1 << bit_position)

                if kth_bit != 0:
                    count += 1
            
            if count % 3 == 1:
                result = result | (1 << bit_position)
        
        
        # Handle Negative Number
        INT_MAX = (1 << 31) # (2**31) = 2147483648
        if result >= INT_MAX:
            result = result - (1 << 32)

        return result
    

# -------------------- Sort --------------------
# Tc: O(nlogn) | Sc: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)

        for i in range(1, n, 3):
            if nums[i] != nums[i-1]:
                return nums[i-1]
        
        return nums[-1]