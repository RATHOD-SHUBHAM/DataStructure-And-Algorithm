class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        # setting the range limit
        left = 1
        right = max(piles)

        k = math.inf

        while left <= right:
            # Current rate
            mid = left + (right - left) // 2

            # Time taken to eat all bananas at current rate
            # If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile/mid)

            if time_taken <= h:
                k = min(k, mid)
                # Further move towards left to find minimum rate
                right = mid - 1
            else:
                left = mid + 1
        
        return k
