'''
442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?


'''
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict = {}
        result = []

        for i in range(len(nums)):
            if nums[i] in dict:
                result.append(nums[i])

            else:
                dict[nums[i]] = i

        return result


def main():
    S = Solution()
    nums = [4,3,2,7,8,2,3,1]
    myfunc = S.findDuplicates(nums)
    print(myfunc)


if __name__ == '__main__':
    main()
