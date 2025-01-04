from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Grab the count/frequency of input.

        # freq_of_input = {}
        # for num in nums:
        #     if num not in freq_of_input:
        #         freq_of_input[num] = 0
            
        #     freq_of_input[num] += 1
        
        freq_of_input = Counter(nums)

        # Add them to freq tables -> [1,1,1,1] -> n = 4 -> 4 : 1
        freq_table = [[] for _ in range(n+1)]
        
        for value, count in freq_of_input.items():
            freq_table[count].append(value)
        

        # Travers from back to front for -> Larget to smallest
        top_k = []
        for arr in reversed(freq_table):
            for num in arr:
                top_k.append(num)

                if len(top_k) == k:
                    return top_k