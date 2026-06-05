"""
Things that we undestand from the problem statement:
1. 1-indexed array
2. sorted
3. exactly one solution.
"""

# Tc = O(n) and Sc: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        i = 0 # keep track of low end
        j = n - 1 # Keep track of high end

        while i < j:
            cur_sum = numbers[i] + numbers[j]

            if cur_sum > target:
                # Reduce the high end number to reduce the sum
                j -= 1
            elif cur_sum < target:
                # Increase the low end number to increase the sum
                i += 1
            else:
                return [i+1, j+1] # 1 indexed array