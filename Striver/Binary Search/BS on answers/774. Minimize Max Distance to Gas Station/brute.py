class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        n = len(stations)

        # no of gas stations placed between each station
        no_of_new_stations_placed = [0] * (n-1)

        # loop for each station
        for _ in range(k):
            max_dist = -1
            last_placed = -1
            # check which has max distance
            for i in range(n-1):
                # distance between 2 already existing gas station
                dist = stations[i+1] - stations[i]
                # check if new gas station was previously added, if we get the new distace
                new_dist = dist / (no_of_new_stations_placed[i] + 1)

                if new_dist > max_dist:
                    max_dist = new_dist
                    last_placed = i
            
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



