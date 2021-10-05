"""

268. Missing Number
Easy

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

"""


class Solution():
    def __init__(self, nums):
        self.nums = nums

    def missingNumber(self):
        for i in range(len(self.nums) + 1):
            if i not in self.nums:
                return i


def main():
    nums = [3, 0, 1]
    s = Solution(nums)
    print(s.missingNumber())


if __name__ == '__main__':
    main()
