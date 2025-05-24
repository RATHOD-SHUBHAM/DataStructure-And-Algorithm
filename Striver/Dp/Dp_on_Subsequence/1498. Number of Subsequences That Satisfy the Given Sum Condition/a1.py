# ------------------ Recursive --------------------
# Time Complexity: O(2^n)
# Space Complexity: O(n)
class Solution:
    def __init__(self):
        self.count = 0

    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Logic
        def recursion(idx, st):
            # base case
            if idx < 0:
                if st:
                    min_val = min(st)
                    max_val = max(st)

                    if (max_val + min_val) <= target:
                        self.count += 1
                
                return
            
            # take
            st.append(nums[idx])
            recursion(idx-1, st)

            # dont take
            st.pop()
            recursion(idx-1, st)


        idx = n - 1
        st = []
        recursion(idx, st)

        return self.count
    

# ------------------ Clever Approach --------------------

"""
You're taking no_of_subsequence % MOD but then adding it to count without taking modulo again. This means count itself can grow very large and exceed the modulo value.

Computing 2 ** (right - left) can be very expensive and cause overflow

Use pow(2, right - left, MOD) instead of 2 ** (right - left) - this efficiently computes (2^(right-left)) % MOD without overflow
"""

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)

        nums.sort()

        MOD = (10 ** 9) + 7

        left = 0 # consider this to be my minimum number
        right = n - 1

        count = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                no_of_subsequence = pow(2, (right-left), MOD)
                count += no_of_subsequence
                left += 1
            else:
                right -= 1
        
        return count % MOD