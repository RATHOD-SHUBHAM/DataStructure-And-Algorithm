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
