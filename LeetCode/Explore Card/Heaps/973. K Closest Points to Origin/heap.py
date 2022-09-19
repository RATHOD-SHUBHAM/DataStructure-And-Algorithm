# time = O(logn + k)
# because pop operation in heap takes log n time and we pop out k value so log n + k
# space = O(n)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        for x, y  in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        
        # add the value to heap
        heapq.heapify(minHeap)
        
        # pop all the value until k = 0
        res = []
        while k > 0:
            dist, x , y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
            
        return res
            
            