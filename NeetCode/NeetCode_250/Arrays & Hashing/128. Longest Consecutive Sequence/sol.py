"""
The Math

    The outer loop visits each element once: O(N) iterations
    The while loop visits each element at most once total (across all iterations of the outer loop)

Think of it this way:

    Each number can only be part of the while loop when we're at the start of its sequence
    Once processed as part of a sequence, we skip it in future outer loop iterations (because val - 1 exists)

    Total operations: At most 2N lookups (N from outer loop, N from all while loops combined) = O(N)


Visual Example
For [1, 2, 3, 4, 5]:
- When val = 1 (start): while loop processes 1→2→3→4→5 (5 operations)
- When val = 2: skipped (because 1 exists)
- When val = 3: skipped (because 2 exists)
- When val = 4: skipped (because 3 exists)
- When val = 5: skipped (because 4 exists)

Total: 5 outer iterations + 5 while operations = 10 operations for 5 elements = O(N)
The while loop doesn't run N times per iteration — it runs N times in total across all iterations!
"""

# Sc: O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        max_seq = 0

        nums_set = set(nums) # Prevents duplicate from looking for consequtive seq again

        for val in nums_set:

            # If there is already an element before this, that will contribute for more length and will include this element, so there is no need to count again
            if val - 1 in nums_set:
                continue
            
            count = 1
            while val + 1 in nums_set:
                count += 1
                val += 1
            

            max_seq = max(max_seq, count)
        

        return max_seq