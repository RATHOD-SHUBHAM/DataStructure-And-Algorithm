from typing import List


class Solution():
    def maxSubArray(self, nums: List[int]) -> int:
        total_sum = nums[0]
        max_result = nums[0]
        for i in nums[1:]:
            total_sum = max(total_sum+i,i)
            print("The total sum is: ",total_sum)
            max_result = max(max_result,total_sum)
            print("Maximum result is: ",max_result)
        return max_result


def main():
    nums = [-2,-1]
    # nums = [1, 12, -5, -6, 50, 3]
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-2]
    s = Solution()
    my_func = s.maxSubArray(nums)
    print("The Final result is : ",my_func)


if __name__ == '__main__':
    main()
