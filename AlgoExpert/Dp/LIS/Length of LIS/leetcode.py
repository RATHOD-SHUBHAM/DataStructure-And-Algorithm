'''

300. Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


'''

# Binary Search
# Time: O(nlogn)
# Space: O(n)

# this question only finds the length of LIS and not LIS array
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = []
        
        for num in nums:
            left = self.binary_search(LIS,num)
            
            if left == len(LIS):
                LIS.append(num)
            else:
                LIS[left] = num
        print(LIS)
        
        return len(LIS)
        
    def binary_search(self, LIS,num):
        left = 0
        right = len(LIS) -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if LIS[mid] == num:
                return mid
            elif LIS[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return left
        