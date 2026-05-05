# Note that positive integers are greater than zero.

'''
For an array of length n, if the array does not contain all of the integers in the range 1 to n+1, the smallest missing positive integer is the first integer missing from that range.

eg: range [1, n+1]
[1,2,3] -> range [1,4] > missing 4
[2,3,4] -> range [1,4] > missing 1
[7,8,9,11,12] -> range [1,6] > missing 1
'''

# Tc and Sc :O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        max_range = n+1

        num_set = set(nums) # O(n)

        for x in range(1, max_range+1): # max_range + 1 because if n = 3, we need to traverse 3 as well.
            if x not in num_set:
                return x 
            
# If a value is not at its corresponding index, then that is the missing element


# ------------------------- Visited Marking Approach -------------------------

# Tc: O(n) Sc :O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: replace negatives with 0
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        # Step 2: mark visited indices
        for i in range(n):
            val = abs(nums[i])
            idx = val - 1 # map value → index (1→0, 2→1, 3→2, ...)

            if idx < 0 or idx >= n: 
                continue

            if nums[idx] > 0:
                nums[idx] *= -1 # mark visited: flip to negative

            elif nums[idx] == 0:
                nums[idx] = -(n + 1) # special sentinel for zero slots:
                                    # negative (= visited) but abs() gives n+1, which is out of bounds and safely
                                    # ignored in this loop if seen again

        # Step 3: find first unvisited index
        for x in range(1, n + 1):
            idx = x - 1
            if nums[idx] >= 0:  # 0 or positive = not visited
                return x

        # --- Step 4: Fallback ---
        # All numbers 1..n are present, so the answer is n+1.
        return n + 1  # all 1..n present, answer is n+1
    
# ------------------------- Cycle Sort Approach -------------------------

# Cycle sort in range
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0

        # Step 1: Cycle sort to place elemnent in correct position
        while i < n:
            correct_idx = nums[i] - 1 # elements correct position in array
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                # if element is not in its place, then place it at its correct idx
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            
            else:
                i += 1
        
        # Step 2: Loop through to find the missing element
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: fall back
        return n+1