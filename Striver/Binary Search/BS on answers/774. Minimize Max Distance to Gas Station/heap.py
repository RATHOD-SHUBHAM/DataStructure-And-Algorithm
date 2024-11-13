class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        n = len(stations)

        # no of gas stations placed between each station
        no_of_new_stations_placed = [0] * (n-1)

        # loop for each station
        for _ in range(k):
            max_dist = -1
            last_placed = -1

            # ------------------- Can replace this max with max heap? -------------------
            # check which has max distance 
            for i in range(n-1):
                # distance between 2 already existing gas station
                dist = stations[i+1] - stations[i]
                # check if new gas station was previously added, if we get the new distace
                new_dist = dist / (no_of_new_stations_placed[i] + 1)

                if new_dist > max_dist:
                    max_dist = new_dist
                    last_placed = i
            # -------------------  -------------------
            
            # New gas station will be placed in between idx i and i + 1
            no_of_new_stations_placed[last_placed] += 1
        
        print("After placing all k new gas station: ",no_of_new_stations_placed)

        # Get the max distance after placing the gas station
        max_dist = -1
        for i in range(n-1):
            # distance between 2 already existing gas station
            dist = stations[i+1] - stations[i]
            # check if new gas station was previously added, if we get the new distace
            new_dist = dist / (no_of_new_stations_placed[i] + 1)
            max_dist = max(max_dist, new_dist)
        
        return max_dist
    

# ---------------------- Heap solution after replacing ----------------------
import heapq
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        n = len(stations)

        # no of gas stations placed between each station
        no_of_new_stations_placed = [0] * (n-1)

        # insert initial distance between 2 gas station into heap
        heap_q = []
        heapq.heapify(heap_q)
        for i in range(n-1):
            dist = stations[i + 1] - stations[i]
            heapq.heappush(heap_q, [-dist, i])
        # print(heap_q)


        # loop for each station
        for _ in range(k):
            # get the max distance between 2 gas station from the heap
            max_heap = heapq.heappop(heap_q)
            idx = max_heap[1]

            # since this is the max distance , add a gas station here
            no_of_new_stations_placed[idx] += 1

            # Calculate the distance after adding the new gas station
            dist = stations[idx+1] - stations[idx]
            new_dist =  dist / (no_of_new_stations_placed[idx] + 1)

            # Add this to the Max heap
            heapq.heappush(heap_q, [-new_dist, idx])
        
        # print(heap_q)
        max_heap = heapq.heappop(heap_q)
        max_dist = -1 * max_heap[0]

        return max_dist
            

