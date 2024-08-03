'''
Compare prev element to current element

prev ele = nums[i-1]
cur ele = nums[i]

If prev_ele > cur_ele : Then this is a break point

If there are more than 1 break point then we cant form a sorted array

To compare last element to first element -  we can use % operator

nums[(i-1) % n]

Example : If we have 4 ele: n=4 , nums = [2,1,3,4]


when i = 0 -> (i-1) % 4 = (-1 % 4) = 3
so nums[0] compare with nums[3]

i = 1 -> (i-1) % 4 = (0) % 4 = 0
nums[1] == nums[0]

and so on..

'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # count no of inflation/break points
        count = 0

        for i in range(n):
            # Compare every element to its previous element - also compare the last element to the first element.
            if nums[(i-1) % n] > nums[i]:        
                count += 1

            if count > 1:
                # if break point greater than one, array cant be rotated
                return False
        
        return True