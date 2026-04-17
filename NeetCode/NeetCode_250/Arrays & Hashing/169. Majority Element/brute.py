# Tc: O(n) | Sc: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums) # O(n)
        
        val = max(counter.values()) # counter.values(): O(K) + max: O(k)
        
        for key, value in counter.items(): #O(k)
            if value == val:
                return key
        
        #  together: $O(n) + O(k) + O(k) + O(k).
        # Sc: O(n)



"""
Can we do better?
While O(n) time is the fastest possible (you must look at every number at least once), you can actually solve this in O(1) space (constant memory) using an algorithm called Boyer-Moore Voting Algorithm.

Boyer-Moore Logic:
- Maintain a candidate and a count.
- Iterate through nums.
- If count is 0, pick the current number as the new candidate.
- If the current number matches candidate, increment count; otherwise, decrement it.

The survivor at the end is the majority element!
"""