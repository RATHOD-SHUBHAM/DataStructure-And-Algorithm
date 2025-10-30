class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # No of banana's KoKo can eat in one hour
        left = 1 # start with 1 banana in hour
        right = max(piles) # max banana in 1 hour

        while left < right:
            mid = left + (right - left) // 2 # first try these many bananas

            # Calculate the time taken to eat all the bananas with mid speed
            time_taken = 0

            for pile in piles:
                time_taken += math.ceil(pile / mid)
            

            # Check if i am able to eat all the bananas at mid pace in the given time
            if time_taken > h:
                # if i am taking more time - then increase pace
                left = mid + 1
            else:
                # Reduce pace
                # time_taken <= h
                '''
                    If Koko can finish all the piles within h hours, set right equal to middle signifying that all speeds greater than middle are workable but less desirable by Koko.
                '''
                right = mid
        
        return left # Right