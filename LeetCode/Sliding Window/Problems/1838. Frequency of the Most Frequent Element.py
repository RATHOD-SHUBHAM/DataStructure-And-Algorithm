# https://www.youtube.com/watch?v=vgBrQ0NM5vE&list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV&index=7

'''
1838. Frequency of the Most Frequent Element

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

 

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 105


'''

#  Check --- > If I change every element of array in such a way that it should match the right element of the array. --> How many extra values will i need.

# To check the extra values ---> compare the sum of elements (by changing it to right element) -- to actual sum + additional K value


# sort the array -- so it will be easy to move and remove the elements

# if all my elements in array become 2 then its sum will be
# [2,2,2] = 2 * 3 --> where 3 is the window size

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        # sort
        nums.sort()
        
        left = right = eleSum = maxWindow = 0
        
        while right < len(nums):
            eleSum += nums[right]
            
            # if total sum of all elements becomes greater than actual sum + k -- then we cant change the value
            while nums[right] * (right-left+1) > eleSum + k:
                eleSum -= nums[left]
                left += 1
            
            # once the valid window is obtained calculate the window size
            maxWindow = max(maxWindow,right-left+1)
                
            right += 1
        
        return maxWindow