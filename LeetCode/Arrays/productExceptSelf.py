from typing import List
# brute force method is take product of all elements and divide it with the index. for each position.

class Solution():
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        print(left)

        # for loop will start from index 1 to 3
        # [ 1 , 2 , 3 , 4 ] ---> len = 4
        #   0   1   2   3   ----> index
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
        print("left list is : ",left)

        right = [1]*len(nums)
        print(right)

        # for loop will start from 2 to 0 and -1 will  take it in reverse order
        # [ 1 , 2 , 3 , 4 ] ---> len = 4           len(nums) - 2 = 4-2 = 2
        #   0   1   2   3   ----> index
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        print("right list is: ",right)

        result = [1]*len(nums)
        for i in range(len(nums)):
            result[i] = left[i] * right[i]

        return result


def main():
    nums = [1, 2, 3, 4]
    s = Solution()
    my_func = s.productExceptSelf(nums)
    print("The Final result is : ",my_func)


if __name__ == '__main__':
    main()
