'''
137. Single Number II

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.

'''
# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ones = twos = 0 
        ones, twos = 0 , 0
        
        for i in nums:
            ones = ~twos & (i ^ ones)
            twos = ~ones & (i ^ twos)
        
        return ones



'''
# Explanation:

nums = [ 2, 2, 3, 2]
         i

ones = 0  --> binary = 00
twos = 0  --> binary = 00
# i = 0 --> nums[i] = 2 --> binary = 10

step 1 -  XOR:
ones ^ nums[i]=

10
00 
--
10  == 2
--
 
step 2 -- negate two and perfom and with result

11  = ~(00)
10 & 
--
10  ==  ones
--


# Similaryly for twos
ones = 10 twos = 00
step 1 -  XOR:
twos ^ nums[i]=

10
00 
--
10  == 2
--
 
step 2 -- negate one and perfom and with result

01  = ~(10)
10 & 
--
00  ==  twos
--


at the end of first iteration for nums[i] = 2, ones = 2 and twos = 0

-------------------------------------------------------------------------
 when we continue iteration
 
 if there is a unique digit --> it will be stored in ones.
 if there are 2 duplicate --> it will be stored in twos.
 if there are 3 duplicate --> it will not be saved any where both ones and twos will be zero



'''