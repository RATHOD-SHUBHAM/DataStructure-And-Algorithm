# time = O(n + k)
# Space = O(n)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = [] # space = O(n)
        
        # time = O(n)
        for i in range(len(arr)):
            dist = abs(x - arr[i])
            heapq.heappush(minHeap, (dist,arr[i]))
            
        res = []
        # Time = O(k)
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
            

        return sorted(res)