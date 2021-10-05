'''
leet Code question : 33

You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
'''
from typing import List


class Solutions:
    def search(self, nums: List, target: int) -> int:
        # if there is nothing in list return -1
        if not nums: return -1

        # if there is just one element and that element is the target then return that element
        if len(nums) == 1 and target in nums: return 0

        left = 0
        right = len(nums) - 1

        if target in nums:
            # if the element is in list are already sorted
            if nums[left] < nums[right]:
                for i in range(len(nums)):
                    if target == nums[i]: return i
            # if the element in the list are not sorted
            else:
                while left <= right:
                    mid = int(left + (right - left) / 2)
                    if target == nums[mid]: return mid

                    if nums[left] <= nums[mid]:
                        if nums[left] <= target <= nums[mid]:
                            right = mid - 1
                        else:
                            left = mid + 1
                    else:
                        if nums[mid] <= target <= nums[right]:
                            left = mid + 1
                        else:
                            right = mid - 1
        else:
            return -1


def main():
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [1]
    # nums = [1, 3]
    # nums = [1]
    nums = [3, 1]
    # target = 0
    # target = 3
    target = 1
    s = Solutions()
    myfunc = s.search(nums, target)
    print(myfunc)


if __name__ == '__main__':
    main()

'''

nums = [4, 5, 6, 7, 0, 1, 2]
case 1 : suppose 7 is the mid point
    [4, 5, 6,   7,    0, 1, 2]
    
    Here left element is smaller than mid. So we know that all element from left to mid is sorted, 
    so we consider [4, 5, 6,7] this to be first array where we perform search
    
    then we perform search on [0,1,2]
    
Case 2: suppose 0 is our mid point
    [4, 5, 6, 7,   0,    1, 2]
    
    here left > mid . we check the right element here. 
    so mid should be less than right. By this we will know that  all element from mid to right is sorted 
    consider that to be first array to search.
     [0, 1, 2]
     
     then search :
     [4, 5, 6, 7]

'''