# ---------- Collection -----------------
import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        count_s = collections.Counter(s)

        final_op = ""
        # most common will given highest count first
        for val, idx in count_s.most_common():
            final_op += (val * idx)
        
        return final_op
    

# ------------- Bucket Sort ---------------

# Bucket Sort
import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        count_s = collections.Counter(s)

        buckets = [[] for _ in range(len(s) + 1)]
        for val, idx in count_s.items():
            buckets[idx].append(val)


        final_op = ""
        for i in reversed(range(len(buckets))):
            bucket = buckets[i]
            for ele in bucket:
                final_op += (ele) * i

        return final_op