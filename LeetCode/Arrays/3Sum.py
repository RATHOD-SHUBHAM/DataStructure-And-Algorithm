"""
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
"""
from typing import List


class Solution():
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This is a 2 pointer solution so lets sort the list. As 2 pointer works better with the sorted list
        nums.sort()
        print("The sorted array is: ",nums)
        # create a list to store the result
        output = []

        # iterate till the last second element because after we will have 2 pointer remaining in the end
        for i in range(len(nums)- 2):
            # print("the index is: ",i)
            # print("The element at that index is: ",nums[i])
            # now we will check tom keep our list unique. So our elements inside the list doesnot match
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            # continue will skip the step --> once continue is encountered control goes back to the for loop and then
            # move forward with the next element.

            left_pointer = i + 1
            right_pointer = len(nums) - 1

            # terget = a+b+c = 0 so, b+c = -a ,n here -a will be the target
            target = 0 - nums[i]
            # print("The target is: ",target)

            while left_pointer < right_pointer:
                total = nums[left_pointer] + nums[right_pointer]
                # print("The total is: ",total)

                # if total is greater than target means b+c > -a
                # ie b+c = 5 and a=4 then 5>-4. we need to reduce the total
                # this can be done by reducing the right pointer as it points to highest value in sorted list
                if total > target:
                    right_pointer -= 1
                elif total < target:
                    left_pointer += 1
                else:
                    output.append([nums[i],nums[left_pointer],nums[right_pointer]])
                    # print(output)
                    # since we cant have duplicate value
                    # or in order to prevent from using the same variable twice

                    # [0,0,0] in such case left pointer and right pointer will collide
                    # if i use if statement it will just move one step and come out.
                    # but we need to move forward as long as we see a new element
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer+1]:
                        left_pointer += 1
                    while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer-1]:
                        right_pointer -= 1

                    left_pointer += 1
                    right_pointer -= 1
        return output


def main():
    s = Solution()
    # nums = [-1, 0, 1, 2, -1, -4]

    nums = [-2, 0, 3, -1, 4, 0, 3, 4, 1, 1, 1, -3, -5, 4, 0]
    myfunc = s.threeSum(nums)
    print(myfunc)


if __name__ == '__main__':
    main()
