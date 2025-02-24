"""
Given a list of integers, write a  function to find the peak in the list. 
A peak is an element which is greater than its neighbors.


There is always a peak in the list. The list contains only one peaks, in case there is no peak return -1.

Eg: [1, 2, 3, 1] => 3


https://www.youtube.com/watch?v=0c3IYL2Scu8&t=524s
"""

from typing import List

# Brute Force
# Tc: O(n) | Sc: O(1)
# class Solution:
#     def findPeak(self, nums:List[int]) -> int:
#         if not nums:
#             return -1

#         return max(nums)

# Binary Search
# Tc: O(logn) | Sc: O(1)
class Solution:
    def findPeak(self, nums:List[int]) -> int:
        if not nums:
            return -1

        n = len(nums)

        left = 0
        right = n - 1


        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1

        return nums[left] # right
        


if __name__ == "__main__":
    obj = Solution()

    # Test Cases 1
    arr = [1, 2, 3, 1]
    op = obj.findPeak(arr)
    print("Solution for test case 1: ", op) # 3

    # Test Cases 2
    arr = [1, 2, 1, 3, 5, 6, 4]
    op = obj.findPeak(arr)
    print("Solution for test case 2: ", op) # 6

    # Test Cases 3
    arr = [1, 2, 3, 4, 5, 6]
    op = obj.findPeak(arr)
    print("Solution for test case 3: ", op) # 6

    # Test Cases 4
    arr = [6, 5, 4, 3, 2, 1]
    op = obj.findPeak(arr)
    print("Solution for test case 4: ", op) # 6

    # Test Cases 5
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    op = obj.findPeak(arr)
    print("Solution for test case 5: ", op) # 5

    # Test Cases 6
    arr = []
    op = obj.findPeak(arr)
    print("Solution for test case 6: ", op) # -1

    # Test Cases 7
    arr = [1]
    op = obj.findPeak(arr)
    print("Solution for test case 7: ", op) # 1

    # Test Cases 8
    arr = [1, 2]
    op = obj.findPeak(arr)
    print("Solution for test case 8: ", op) # 2

    # Test Cases 9
    arr = [2, 1]
    op = obj.findPeak(arr)
    print("Solution for test case 9: ", op) # 2

    # Test Cases 10
    arr = [1,3,4,5,6,7,8,4,3,2,1]
    op = obj.findPeak(arr)
    print("Solution for test case 10: ", op) # 8
    

print("=====================================================================================================")
print("List may contain duplicates")
print("=====================================================================================================")
# If there are duplicates, then the above solution will not work.
# In that case, we need to use the below solution


class Solution1:
    def findPeakWithDuplicate(self, nums:List[int]) -> int:
        if not nums:
            return -1

        n = len(nums)

        left = 0
        right = n - 1


        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                ptr = mid + 1

                while ptr < right and nums[mid] == nums[ptr]:
                    ptr += 1
                
                if ptr == right:
                    right = mid
                elif nums[mid] > nums[ptr]:
                    right = mid
                elif nums[mid] < nums[ptr]:
                    left = ptr

        return nums[left] # right
    

if __name__ == "__main__":
    obj = Solution1()

    # Test Cases 1
    arr = [1, 2, 3, 3, 3, 3, 1]
    op = obj.findPeakWithDuplicate(arr)
    print("Solution for test case 1: ", op) # 3

    # Test Cases 2
    arr = [1,3,7,6,6,6,6,4,3,2,1]
    op = obj.findPeakWithDuplicate(arr)
    print("Solution for test case 2: ", op) # 7

    # Test Cases 3
    arr = [1, 2, 3, 3, 3, 3, 3]
    op = obj.findPeakWithDuplicate(arr)
    print("Solution for test case 3: ", op) # 3

    # Test Cases 4
    arr = [1, 2, 3, 3, 3, 3, 1]
    op = obj.findPeakWithDuplicate(arr)
    print("Solution for test case 4: ", op) # 3

    # Test Cases 5
    arr = [6,6,6,6,6,6,6]
    op = obj.findPeakWithDuplicate(arr)
    print("Solution for test case 5: ", op) # 6

    # Test Cases 6
    arr = []
    op = obj.findPeakWithDuplicate(arr)
    print("Solution for test case 6: ", op) # -1

    # Test Cases 7
    arr = [6,6,6,6,6,6,6,6,5,4,3,2,1]
    op = obj.findPeakWithDuplicate(arr)
    print("Solution for test case 7: ", op) # 6

    # Test Cases 8
    arr = [1, 6, 6, 6, 6, 6, 5]
    op = obj.findPeakWithDuplicate(arr)
    print("Solution for test case 8: ", op) # 6
