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
    def insertionSort(self, num):
        n = len(num)

        for _ in range(n):
            for i in range(1, n):
                if num[i] < num[i-1]:
                    # Swap the elements
                    num[i], num[i-1] = num[i-1], num[i]
        
        return num


    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        min_val = min(nums)
        max_val = max(nums)

        # Edge case: all elements are the same
        if min_val == max_val:
            return nums

        # Step 1: Create n buckets
        buckets = [[] for _ in range(n)]

        # Step 2: Distribute elements into buckets
        for num in nums:
            # Normalize to [0, 1) then scale to bucket index
            normalize = (num - min_val) / (max_val - min_val) # maps to [0.0, 1.0]
            idx = int(normalize * (n-1))  # maps to [0, n-1]
            buckets[idx].append(num)
        
        # Step 3: Sort each bucket and concatenate
        output = []
        for bucket in buckets:
            # output.extend(sorted(bucket))  # Timsort on small buckets
            num = self.insertionSort(bucket) # insertion sort
            output.extend(num)
        return output