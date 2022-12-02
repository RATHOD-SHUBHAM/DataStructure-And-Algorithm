'''
Logic: get the range of number with in which the value difference will get satisfied

eg: number 9 and valueDiff = 3

so 9 - 3 = 6
and 9 + 3 = 12

so any number with in the range [6,12] when subtracted with 9, will have a difference <= 3

eg 
9-6 = 3
9-7 = 2
9-8 = 1
9-9=0
10-9 = 1
11-9 = 2
12-9 = 3


https://www.youtube.com/watch?v=pPiSMPWKZ3E&ab_channel=JoeJames
bisect_left(val) returns the index of val in the list if it were inserted at the leftmost position in sorted order. This is the same as the number of elements strictly less than val. (called a rank query on the binary search Wikipedia page)

bisect_right(val) returns the index of val in the list if it were inserted at the rightmost position in sorted order. This is the same as the number of elements less than or equal to val.

diff = 0
sorted num = []
num = [1,2,3,1]

left = n - diff
right = n + diff

i = 1

left:  1
p1:  0 -> left index at which 1 might get inserted
right:  1 -> right index at which 1 might get inserted
p2:  0

if p2 - p2 is 0 then there is no range.
p2 - p1 :  0


i = 2
sorted num = [1]
num = [1,2,3,1]
left:  2
p1:  1 = 2 will be inserted after 1
right:  2
p2:  1 = 2 will be inserted after 1
p2 - p1 :  0


i = 3
sorted num = [1,2]
num = [1,2,3,1]
left:  3
p1:  2 = 3 will be inserted after 2 ie idx 1, so idx wil be 2
right:  3
p2:  2 = 3 will be inserted after 2 ie idx 1, so idx wil be 2
p2 - p1 :  0

i = 4
sorted num = [1,2,3]
num = [1,2,3,1]
left:  1
p1:  0 = 1 will be inserted at index 0
right:  1
p2:  1 = i will be inserted to right of 0

so range is [0,1] = and we ahve element in range 01
p2 - p1 :  1
'''


from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        sortedNumber = SortedList() # this will give the range of number i - diff , i + diff
        
        for idx, num in enumerate(nums):
            print("sortedNumber: ",sortedNumber)
            
            if idx > indexDiff:
                # remove the number out of bound number from sorted list
                sortedNumber.remove(nums[idx - (indexDiff + 1)])
                print("sortedNumber after removal: ",sortedNumber)
                
            # check for the left and right range
            left = num - valueDiff
            right = num + valueDiff
            
            print("left: ",left)
            print("right: ",right)
            
            # get the point of insertion in the sorted list
            # left point can be <= num
            # right point will be grater than >
            point_1 = sortedNumber.bisect_left(left) # return index where left can be inserted
            print("index to be inserted on left of value: ", point_1)
            point_2 = sortedNumber.bisect_right(right) # return index where right can be inserted
            print("index to be inserted on right of value: ", point_2)
            
            # if there is no subtractable range. then point 2 - point 2 = 0
            print("point_2 - point_1 : ",point_2 - point_1)
            if point_2 - point_1 > 0:
                return True
            
            sortedNumber.add(num)
            print("\n")
            
        return False