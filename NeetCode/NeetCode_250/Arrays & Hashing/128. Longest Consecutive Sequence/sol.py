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

# Tc and Sc: O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = 0

        # Convert list to set for O(1) average-time lookups
        # Also removes duplicate values automatically
        num_set = set(nums)

        # Iterate over the SET instead of the original list
        # to avoid processing duplicate numbers unnecessarily
        for num in num_set:
            prev_num = num - 1

            # Only start counting from the BEGINNING of a sequence
            # If (num - 1) exists, then `num` is not a sequence start → skip
            if prev_num in num_set:
                continue
            
            # `num` is a sequence start, so count forward
            count = 1
            while num + 1 in num_set:
                count += 1
                num += 1  # move to next consecutive number
            
            # Update the global maximum
            max_count = max(max_count, count)
        
        return max_count