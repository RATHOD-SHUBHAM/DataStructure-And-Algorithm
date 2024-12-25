import heapq
import math

class Solution:
    def getDistance(self, points):
        x1 = 0
        y1 = 0

        distance_array = []

        heapq.heapify(distance_array)

        for i in range(len(points)):
            x2 , y2 = points[i]

            cur_dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            heapq.heappush(distance_array, (cur_dist, i))
        
        return distance_array

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_array = self.getDistance(points)

        # print(distance_array)

        op = []
        for _ in range(k):
            dist, idx = heapq.heappop(distance_array)
            op.append(points[idx])
        
        return op