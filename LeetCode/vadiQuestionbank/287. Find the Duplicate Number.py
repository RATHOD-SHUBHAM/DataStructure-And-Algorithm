'''

287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

'''
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            print(dict)
            # print(nums[i])
            if nums[i] in dict:
                return nums[i]
            else:
                dict[nums[i]] = i


def main():
    nums = [1, 3, 4, 2, 2]
    # nums = [3, 1, 3, 4, 2]
    cla_ss = Solution()
    my_func = cla_ss.findDuplicate(nums)
    print("final result is : ",my_func)



if __name__ == '__main__':
    main()
