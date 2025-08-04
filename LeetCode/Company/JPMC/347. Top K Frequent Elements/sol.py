class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ele : count
        freq_count = collections.Counter(nums)

        # List[List]
        n = max(freq_count.values())
        freq_table = [[] for _ in range(n+1)]
        for value, count in freq_count.items():
            freq_table[count].append(value)
        
        top_k = []
        for freq_arr in reversed(freq_table):
            for ele in freq_arr:
                top_k.append(ele)

                if len(top_k) == k:
                    return top_k