# Tc:O(nlogn)| Sc: O(n + k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the freq of nums
        counter = Counter(nums)
        # print(counter)

        # push the freq and num to max heap
        heap = []

        # implementing maxheap
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))

        # pop the k most freq elements
        top_k = []
        for _ in range(k):
            val = heapq.heappop(heap)
            # print(val)
            # print(type(val))

            top_k.append(val[1])
        
        return top_k

        