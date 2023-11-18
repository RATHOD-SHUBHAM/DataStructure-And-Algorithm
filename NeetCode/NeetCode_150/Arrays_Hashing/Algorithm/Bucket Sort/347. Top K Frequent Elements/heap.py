class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)

        maxHeap = []
        heapq.heapify(maxHeap)

        # print(counter)
        for num, count in counter.items():
            heapq.heappush(maxHeap, (-count, num))
        
        # print(maxHeap)

        ans = []
        while k != 0:
            count , num = heapq.heappop(maxHeap)
            ans.append(num)
            k -= 1
        
        return ans