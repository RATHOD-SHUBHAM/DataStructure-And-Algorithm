# Freq Sort Logic

# Tc:O(n) | Sc: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        count = collections.Counter(nums)

        freq = [-math.inf] * (n+1)
        for key, cnt in count.items():
            freq[cnt] = key
        

        for ele in reversed(freq):
            if ele == -math.inf:
                continue
            else:
                return ele
            
# ---------------------------------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------------------------------

"""
Boyer-Moore Logic:

1. Maintain a candidate and a count.

2. Iterate through nums.

3. If count is 0, pick the current number as the new candidate.

4. If the current number matches candidate, increment count; otherwise, decrement it.

The survivor at the end is the majority element!
"""


# Tc:O(n) | Sc: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        maj_ele = 0

        for i in range(n):
            # If the count becomes 0, mark this as new beginning of maj ele as per voting
            if count == 0:
                count = 1
                maj_ele = nums[i]
            
            # Voting
            else:
                if maj_ele == nums[i]: # if the val is same: increase count
                    count += 1
                else:
                    count -= 1 # if they are different : decrease count
        
        return maj_ele
