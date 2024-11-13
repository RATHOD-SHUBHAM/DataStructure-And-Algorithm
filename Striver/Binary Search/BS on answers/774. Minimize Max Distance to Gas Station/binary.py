from typing import List
import math

class Solution:
    def getGasStationCount(self, stations, interval, n):
        # No of gas stations that can be placed
        cnt_of_gas_stations = 0

        for i in range(n-1):
            actual_dist = stations[i+1] - stations[i]
            no_of_new_gas_station = actual_dist / interval
            
            # Check if the actual placment is possible and is not on top or overflowing outside
            # Eg: 1/0.4 = 2.5 -> but we can only place 2 logically
            cnt_of_gas_stations += math.floor(no_of_new_gas_station)
        
        return cnt_of_gas_stations


    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        n = len(stations)

        low = 0
        high = 0 

        for i in range(n-1):
            dist = stations[i+1] - stations[i]
            high = max(high, dist)

        
        power =  1e-6 # 10 power -6
        while high - low > power:
            mid = (low + high) / 2 # this will be the current distance we check on

            # No of gas stations that can be placed
            cnt_of_gas_stations = self.getGasStationCount(stations, mid, n)

            if cnt_of_gas_stations <= k:
                high = mid
            else:
                low = mid

        return low