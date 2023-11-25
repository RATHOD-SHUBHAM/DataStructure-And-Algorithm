class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = []
        heapq.heapify(maxHeap)

        # add stones to maxHeap
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)

            if x == y:
                continue
            else:
                y *= -1
                x *= -1
                new_stone = y - x

                new_stone *= -1
                heapq.heappush(maxHeap, new_stone)
        
        # print(maxHeap)
        return -1 * maxHeap[0] if maxHeap else 0