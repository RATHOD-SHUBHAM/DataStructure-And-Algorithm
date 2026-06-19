"""
Hashmap solution is salvageable but you'll fight duplicates the whole way. 
In an interview, if you go down this path you'll spend more time on dedup logic than the actual problem.
"""

# Tc: O(n^2) | Sc: O(n)
"""
twoSum is O(n), and we call it n times.

Sorting the array takes O(nlogn), so overall complexity is O(nlogn + n^2). This is asymptotically equivalent to O(n^2).
"""
class Solution:
    def __init__(self):
        self.op = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                break

            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(i, n, nums)
        
        return self.op
    
    def twoSum(self, i, n, nums):
        left = i + 1
        right = n - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]

            if cur_sum == 0:
                self.op.append([nums[i] , nums[left] , nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                
            elif cur_sum < 0:
                left += 1
            
            else:
                right -= 1
        