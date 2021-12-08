'''

643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

'''

# time complexity: O(n), 
# space complexity: O(1)


'''
First window sum = [1,12,-5,-6,50,3]
                    ^.       ^
                    
Second window sum = 
[1,12,-5,-6,50,3]
 i  ^.    ^  j
 
step 1 : subtract i from previous window
Step 2 : Add j from previous window

'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k])
        maxSum = curSum
        
        # add the next element by deleting the first element
        for i in range(k,len(nums)):
            # step 1: delete the first element from window
            curSum -= nums[i-k]
            
            # step 2: Add the next element to the window
            curSum += nums[i]
            
            if curSum > maxSum:
                maxSum = curSum
                
        return maxSum / k