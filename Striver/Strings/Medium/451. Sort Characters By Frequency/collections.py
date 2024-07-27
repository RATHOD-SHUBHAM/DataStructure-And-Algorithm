# Collection
import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        count_s = collections.Counter(s)

        final_op = ""
        # most common will given highest count first
        for val, idx in count_s.most_common():
            final_op += (val * idx)
        
        return final_op