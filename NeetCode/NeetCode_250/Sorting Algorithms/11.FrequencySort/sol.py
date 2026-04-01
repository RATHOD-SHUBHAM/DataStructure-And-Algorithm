"""
Frequency Sort using HashMap + Bucket Sort:
Core Idea:
1. Count frequency of each element using a HashMap
2. Create buckets where index = frequency
3. Place elements in their frequency bucket
4. Traverse buckets from highest to lowest frequency to build result

Example:
nums = [1,1,1,2,2,3]
freq  = {1:3, 2:2, 3:1}
buckets[3] = [1]
buckets[2] = [2]
buckets[1] = [3]
result = [1,1,1,2,2,3]

TC: O(n)
SC: O(n)
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Count frequency of each element
        freq_count = collections.defaultdict(int)
        for num in nums:
            freq_count[num] = freq_count.get(num, 0) + 1
        
        # Step 2: Create buckets where index = frequency
        # Max frequency can be n (all elements same)
        buckets = [[] for _ in range(n + 1)]

        for num, freq in freq_count.items():
            buckets[freq].append(num)
        
        # print(buckets)

        # Step 3: Traverse buckets from highest to lowest frequency
        output = []
        for freq in reversed(range(n + 1)):
            for num in buckets[freq]:
                output.extend([num] * freq)  # add element freq times
        
        return output