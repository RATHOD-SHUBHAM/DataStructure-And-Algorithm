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

# ---------------------------------------------------------------------------------------
"""
Can you answer this:

Why does this algorithm only work because the majority element is guaranteed to appear more than n/2 times?
What would happen if there was no majority element?

This is a common follow-up interview question — worth thinking about! 🤔

"""
# Tc: O(n) | Sc: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0 # polling
        maj_ele = -math.inf

        for i in range(n):
            if count == 0:
                maj_ele = nums[i]
                count += 1
            
            else:
                if nums[i] == maj_ele:
                    count += 1
                else:
                    count -= 1
        
        # return maj_ele
        
        # The second pass is a verification step — if no majority element exists, you return None implicitly instead of a wrong answer.
        counter = 0
        for num in nums:
            if maj_ele == num:
                counter += 1
        
        if counter > (n/2):
            return maj_ele 
        
## Same as above but with a different implementation of the second pass
# Tc: O(n) | Sc: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0 # polling
        maj_ele = nums[0]

        for num in nums:
            if count == 0:
                maj_ele = num
                
            # Voting
            if num == maj_ele:
                count += 1
            else:
                count -= 1
        
        # The second pass is a verification step — if no majority element exists, you return None implicitly instead of a wrong answer.
        cnt_maj_ele = nums.count(maj_ele)

        if cnt_maj_ele > (n/2):
            return maj_ele
            
