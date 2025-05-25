# Tc: O(n^2)
# Sc: O(1)

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(1, n): # O(n)
            arr_1 = sum(nums[ : i]) # O(n)
            arr_2 = sum(nums[i : ])

            diff = abs(arr_1 - arr_2)

            if diff % 2 == 0:
                count += 1
        
        return count