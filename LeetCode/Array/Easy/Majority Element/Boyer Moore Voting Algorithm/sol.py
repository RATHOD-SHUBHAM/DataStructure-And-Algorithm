'''
## Boyer-Moore Voting Algorithm:

Keep adding 1 --- When ever you see the current element

Subtract 1 --- when ever you dont see the current element. ie current element would have changed.

And 

When the count of element becomes zero. Change the element to current element and increase the count by 1

## Basically 

if there are equal number of element than each number will negate the other number and count will be zero
eg: 1,1,1,2,2,2 = 0 -- because 3 one and 3 twos will negate one other


if one number is more than other -- then larger number will defeate the smaller number count
eg 1,1,2,2,2

then 2 one and 2 twos will negate one other. But there is still one more 2 remaining.
Which says that 2 is our majority element





'''
# Time: O(n)
# Space: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        curr = 0 # or curr = nums[i]
        
        for i in range(len(nums)):
            if count == 0:
                curr = nums[i]
                
            if curr == nums[i]:
                count += 1
            else:
                count -= 1
                
        return curr