# time: O(NlogN)
# Spce: O(n)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert it to max heap
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
            
        # print(stones)
        
        heapq.heapify(stones)
        # print(stones)
        
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            # print(stone_1)
            stone_2 = heapq.heappop(stones)
            # print(stone_2)
            
            
            if stone_1 != stone_2:
                if stone_1 < stone_2:
                    stone = stone_1 - stone_2
                    # print(stone)
                    heapq.heappush(stones ,stone)
                else:
                    stone = stone_2 - stone_1
                    heapq.heappush(stones ,stone)     
            else:
                if len(stones) == 1:
                    return -stones[0]
                elif len(stones) == 0:
                    return 0
                
        if len(stones) == 1:
            return stones[0] * -1
        else:
            return 0