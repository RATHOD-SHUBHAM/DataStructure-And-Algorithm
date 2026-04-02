# Using idea from : 11. Frequency Sort algorithm
# Tc and Sc: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Get the freq of each element
        count = collections.Counter(nums)
        # print(count)

        # Add them in bucket based on the frequency
        freq_bucket = [[] for _ in range(n+1)]
        for ele, freq in count.items():
            freq_bucket[freq].append(ele)
        
        # print(freq_bucket)

        # Extract element from the bucket 
        output = []
        for bucket in reversed(freq_bucket):
            if bucket:
                for ele in bucket:
                    output.append(ele)

                    if len(output) == k:
                        return output


"""
Time & Space Complexity Analysis
-----------

Time Complexity: O(n)

Let's break it down step by step:
* Building count → Counter(nums) iterates through all elements → O(n)
* Building freq_bucket → iterates over unique elements in count → O(n) (at most n unique elements)
* Extracting elements → in the worst case, iterates through all buckets and elements → O(n)

    | Overall: O(n) + O(n) + O(n) = O(n)

This is why bucket sort is preferred here over a heap-based approach (which would be O(n log k)).

-----------

Space Complexity: O(n)

* count dictionary → stores at most n unique elements → O(n)
* freq_bucket → array of size n+1, total elements across all buckets = number of unique elements → O(n)
* output → stores k elements → O(k)

    | Overall: O(n)

-----------

Quick Insight 💡

The key tradeoff here is:

Approach	Time	Space
Bucket Sort O(n)	O(n)    # Current solution
Heap-based	O(n log k)	O(n)

Current approach is optimal for this problem.
"""