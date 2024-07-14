# Just different ways of returning.
import collections
from typing import List

# ------------- First Way to Return --------------------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        counter = collections.Counter(nums)

        buckets = [[] for _ in range(n+1)]
        for val, count in counter.items():
            buckets[count].append(val)



        top_k = []
        for bucket in reversed(buckets):
            for ele in bucket:
                top_k.append(ele)

                if len(top_k) == k:
                    return top_k


# ------------- Second Way to Return --------------------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        counter = collections.Counter(nums)

        buckets = [[] for _ in range(n+1)]
        for val, count in counter.items():
            buckets[count].append(val)



        top_k = []
        for bucket in reversed(buckets):
            for ele in bucket:
                top_k.append(ele)

            if len(top_k) == k:
                return top_k
            
# ------------- Third Way to Return --------------------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        counter = collections.Counter(nums)

        buckets = [[] for _ in range(n+1)]
        for val, count in counter.items():
            buckets[count].append(val)



        top_k = []
        for bucket in reversed(buckets):
            for ele in bucket:
                top_k.append(ele)

            if len(top_k) == k:
                break
        
        return top_k