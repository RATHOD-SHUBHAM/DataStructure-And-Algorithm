# ========================================================================================================================
# First Draft: Basic Code
# ========================================================================================================================

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
            
        p = m - 1
        q = n - 1
        r = (m + n) - 1

        while p >= 0 and q >= 0:
            if nums2[q] > nums1[p]:
                nums1[r] = nums2[q]
                q -= 1
                r -= 1
            else:
                nums1[r] = nums1[p]
                p -= 1
                r -= 1

        # print(nums1)
        """
        Above solution wont work:

        What happens when the while loop ends but q >= 0 still has remaining elements?

        For example:

        nums1 = [4,5,6,0,0,0], m = 3
        nums2 = [1,2,3],       n = 3

        """


# ========================================================================================================================
# Working Solution

# Learning
"""
    1. When merging into one of the input arrays, fill from the back — the empty tail is your safe zone, and you'll never overwrite what you haven't read yet.
    2. Guard against index errors on exhausted pointers.
        Check p < 0 or q < 0 before accessing nums1[p] or nums2[q], not after. Boundary checks come first.
"""
# ========================================================================================================================

# Tc: O(m + n) | Sc: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
            
        p = m - 1
        q = n - 1
        r = (m + n) - 1

        # Fill nums1 from the back — largest element goes in last slot first.
        # Filling backwards avoids overwriting nums1 elements we haven't compared yet.
        while r >= 0:

            # Place nums2[q] if:
            #   * nums1 is exhausted (p < 0), so only nums2 elements remain OR
            #   * q >= 0 guard prevents index error when both pointers are done(< 0),
            #     and nums2's current element is larger
            if p < 0 or (q >= 0 and nums2[q] > nums1[p]):
                nums1[r] = nums2[q]
                q -= 1
                r -= 1

            # Place nums1[p] if:
            #   - nums2 is exhausted (q < 0), so only nums1 elements remain OR
            #   - p >= 0 guard (mirrors above), and nums1's current element
            #     is larger or equal (equal case goes here to keep sort stable)
            elif q < 0 or (p >= 0 and nums1[p] >= nums2[q]):
                nums1[r] = nums1[p]
                p -= 1
                r -= 1



# Using For Loop instead of While Loop   

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = len(nums1)

        p = m - 1
        q = n - 1

        for r in reversed(range(x)):
            if p < 0  or (q >= 0 and nums2[q] > nums1[p]):
                nums1[r] = nums2[q]
                q -= 1

            elif q < 0 or ( p >= 0 and nums1[p] >= nums2[q]):
                nums1[r] = nums1[p]
                p -= 1
