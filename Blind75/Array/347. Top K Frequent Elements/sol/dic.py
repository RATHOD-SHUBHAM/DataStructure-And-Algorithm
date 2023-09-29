# Tc: O(nlogn) | Sc: O(nk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the freq of nums
        freq = collections.defaultdict()

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        # print(freq)

        # push the freq and num to max heap
        heap = []
        for num, frq in freq.items():
            heapq.heappush(heap, (-frq, num))
        

        # pop the k most freq elements
        top_k = []
        for _ in range(k):
            ele = heapq.heappop(heap)
            top_k.append(ele[1])
        
        return top_k