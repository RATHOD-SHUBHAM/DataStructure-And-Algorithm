"""
Bucket Sort:
Core Idea:
Distribute elements into buckets, sort each bucket individually,
then concatenate all buckets together.

Works best when input is:
- Uniformly distributed
- Floating point numbers between 0 and 1 (classic use case)
- Or any range that can be normalized

TC: O(n + k) average, O(n^2) worst case (all elements in one bucket)
SC: O(n + k) where k = number of buckets
"""

class Solution:
    def insertionSort(self, nums):
        n = len(nums)

        for i in range(1, n):
            key = nums[i]

            j= i - 1

            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            
            nums[j+1] = key

        return nums

    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        min_val = min(nums)
        max_val = max(nums)

        # Step 1: Create n buckets
        buckets = [[] for _ in range(n)]

        # Edge case: all elements are the same
        if min_val == max_val:   # avoids division by zero
            return nums



        # Step 2: Distribute elements into buckets
        """
        * num - min_val shifts the smallest value to 0 (handles negatives and offsets).
        * / (max_val - min_val) squashes the range to [0, 1], so the units don’t matter.
        * * (n-1) stretches it to fit the array of buckets.
        """
        for num in nums:
            # Normalize to [0, 1) then scale to bucket index
            normalize = (num - min_val) / (max_val - min_val) # maps to [0.0, 1.0]
            idx = int(normalize * (n - 1)) # maps to [0, n-1]
            buckets[idx].append(num)
        
        
        # Step 3: Sort each bucket and concatenate
        op = []
        for bucket in buckets:
            # sorted_ele = sorted(bucket) # Timsort on small buckets 
            # or
            sorted_ele = self.insertionSort(bucket)
            op.extend(sorted_ele)
        return op