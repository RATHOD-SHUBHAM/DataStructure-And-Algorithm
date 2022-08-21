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
                if stone_1 > stone_2:
                    stone_to_push = stone_1 - stone_2
                else:
                    stone_to_push = stone_2 - stone_1
                    
                # print(stone_to_push)
                
                if stone_to_push != 0:
                    stone_to_push *= -1
                    heapq.heappush(stones , stone_to_push)
                else:
                    if len(stones) == 0:
                        return 0
            else:
                if len(stones) == 0:
                        return 0
                
        if len(stones) == 1:
            return stones[0] * -1
        else:
            return 0