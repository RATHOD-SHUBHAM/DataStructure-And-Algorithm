# Tc: O(nlogm) | Sc: O(1)

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)

        max_val = max(piles)

        left = 1
        right = max_val

        while left < right:
            mid = left + (right - left) // 2 # Rate at which koko will eat banana

            total_time_taken = 0
            for i in range(n):
                time_taken = math.ceil(piles[i] / mid)
                total_time_taken += time_taken


            if total_time_taken <= h:
                # Koko can comfortably finish in given time with this rate, so try to further lower the speed and check
                right = mid
            else:
                left = mid + 1 # increase the rate at which koko eats, so she can finish on time
        
        return left # or right