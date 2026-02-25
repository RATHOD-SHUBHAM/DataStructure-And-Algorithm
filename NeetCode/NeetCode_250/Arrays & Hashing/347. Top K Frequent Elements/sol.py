# Tc and Sc: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        count = collections.Counter(nums) # O(n)

        freq = [[] for _ in range(n+1)]
        
        for key, val in count.items():
            freq[val].append(key)
        
        op = []
        for ele in reversed(freq): # O(n)
            if not ele:
                continue
            
            for ch in ele:
                op.append(ch)

                if len(op) == k:
                    return op