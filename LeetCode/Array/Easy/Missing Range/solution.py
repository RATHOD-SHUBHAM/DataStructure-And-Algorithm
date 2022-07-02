'''
2 Pointer Approach.
String type conversion.


# Things to keep in mind:
    1. Lower and Upper value will always be present.
    2. Nums may or may not be present.

# Walk Through:
    1. Always include lower and upper in the loop.
  Lower + nums + upper. 
  eg = lower = -1.    +    nums[i] = [ 1, 3, 5, 9].   +.  upper =  15
  -1 + [1, 3, 5, 9] + 15 = [1, 3, 5, 9, 15]

To find range we perform:
    nums[i] = [ 1, 3, 5, 9]
    Range:
    3-1. -->. 1+1 = 2
    5-1. -->. 3+1 = 4
    9-1. -->. 5+1 = 6-8

But for lower and upper we have to include the lower and upper value ot get the range:
    lower = -1.    +    nums[i] = [ 1, 3, 5, 9].   +.  upper =  15
    
    Range :
    lower = -1 --> 0 # here if i do lower -1 ill get 0 which is not right. so to negate this only for lower i add 1. lower - 1 + 1
    3-1 --> 1+1 = 2
    5-1 --> 3+1 = 4
    9-1 --> 5+1 = 6-8
    upper = 15 --> 9+1 = 10 # here i need to include upper. If i do upper -1 ill get 14 which is not right. So i negate -1 by adding + 1 = upper -1 +1

'''
from typing import List
class Solution:

    def rangeOfNumber(self, lower, upper):
        if lower == upper:
            return str(lower)
        return str(lower) + "->" + str(upper)


    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        prev = lower - 1

        # add +1 because, once i goes out of bound, i need to include the upper value.
        for i in range(len(nums)+1):
            if i < len(nums):
                curr = nums[i]
            else:
                curr = upper + 1

            if prev + 1 <= curr - 1:
                res.append(self.rangeOfNumber(prev+1, curr-1))

            prev = curr
        
        return res



# Test
if __name__ == "__main__":
    # Test 1
    # nums = [-1, 0, 1, 3, 5, 9]
    # lower = -1
    # upper = 15
    # print(Solution().findMissingRanges(nums, lower, upper))

    # Test 2
    # nums = [] 
    # lower = 1
    # upper = 1
    # print(Solution().findMissingRanges(nums, lower, upper))

    # test 3
    # nums = [] 
    # lower = -3 
    # upper = -1
    # print(Solution().findMissingRanges(nums, lower, upper))


    # Test 4
    # nums = [-1] 
    # lower = -1 
    # upper = -1
    # print(Solution().findMissingRanges(nums, lower, upper))

    # Test 5
    nums = [-1] 
    lower = -2 
    upper = -1
    print(Solution().findMissingRanges(nums, lower, upper))
