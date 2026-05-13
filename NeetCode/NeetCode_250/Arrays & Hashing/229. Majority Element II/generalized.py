"""
The pattern is:

For n/k, you need k-1 candidates.

The reasoning is simple — at most k-1 elements can appear more than n/k times (since k elements each appearing > n/k times would require > n total elements, which is impossible).

"""

class Solution:
    def generalized_majority_Element(self, nums, k=3):
        n = len(nums)
        candidates = {}  # {candidate: count}

        for num in nums:
            if num in candidates:
                candidates[num] += 1
            elif len(candidates) < k - 1:
                candidates[num] = 1
            else:
                # Cancel everyone — the core BM voting step
                candidates = {c: cnt - 1 for c, cnt in candidates.items()}
                # Filter zero values
                candidates = {c: cnt for c, cnt in candidates.items() if cnt > 0}

        # Verification pass
        return [
            c for c in candidates
            if nums.count(c) > n // k
        ]

    def majorityElement(self, nums: List[int]) -> List[int]:
        return self.generalized_majority_Element(nums, k=3)