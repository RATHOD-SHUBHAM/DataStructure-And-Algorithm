'''

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.


Hint 1:
Array was originally in ascending order. Now that the array is rotated, there would be a point in the array where there is a small deflection from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].


Hint 2:
You can divide the search space into two and see which direction to go. Can you think of an algorithm which has O(logN) search complexity?

Hint 3:
All the elements to the left of inflection point > first element of the array.
All the elements to the right of inflection point < first element of the array


'''

# todo : if no run time were specified this could be have been done in one single line
# return max(list)
# since O(logn) is specified lets do a BST


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # -1 if len(nums) == 0 else 1
        print(len(nums))
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]

        # if i have a list so left element will be the start element and right element will be my last element in a list
        left = 0
        right = len(nums) - 1

        # if my last element is greater than my first element then my list is already sorted
        if nums[right] > nums[0]:
            return nums[0]
        #  left index should not cross right index
        while left < right:
            mid = int(left + (right - left) / 2)
            print(" the mid point is : ", mid)
            print(" the mid element is : ", nums[mid])

            # once i get the mid element i need to compare it with my side element
            # if there is a drastic shift then we found our smallest element
            '''
              6 7 2 3 

                consider mid point to be 7
                so 7 is greater than 2

                list is sorted in ascending order but i see a smaller element to the right
                so that will be the smallest element

                return 2


             6 7 2 3
                now consider 2 to be the mid point

                so since the list is in ascending order we know that element before 2 must be smaller than 2
                but here 7 > 2

                so we return 2 as smallest element


            '''
            if nums[mid] > nums[mid + 1]:
                print("the value is: ",mid+1)
                return nums[mid + 1]

            if nums[mid - 1] > nums[mid]:
                print("the value is: ", mid)
                return nums[mid]

            # if my mid element is greater than the starting element then ill have to look in the right subtree
            # if my mid element is smaller than the first element then ill have to look in the left sub tree

            ''' 
                 0 1    2 3 4 5 
                 4 5    6 7 2 3


                 consider 6 to be my mid element

                 if i see 6 is greater than 4

                 so i know everything from 4 to 6 is in increasing order. but i dont know after 6

                 so ill do my search to the right of my mid element 




                 0 1 2 3      4 5 
                 4 5 6 7      2 3

                 Consider mid element to be 2

                 so 4 is greater than 2

                 so here i know after 2 things will increase.

                 so what ill do is ill check for small element to left of my mid point
            '''

            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1


def main():
    s = Solution()
    # nums = [3, 4, 5, 1, 2]
    nums = [4, 5, 6, 7, 2, 3]
    myfunction = s.findMin(nums)
    print(myfunction)


if __name__ == '__main__':
    main()
