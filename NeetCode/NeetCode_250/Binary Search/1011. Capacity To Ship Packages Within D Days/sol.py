# Find the smallest capacity of ship such that all packages can be shipped within d days

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights) # the ship has to be able to carry the heaviest single package, otherwise that package could never be shipped.
        right = sum(weights) # load all the package in one day, so ship weight should be sum of all weights

        ships_weight = left

        while left < right:
            # pick a capacity to test if this can be taken in d days
            mid = left + (right - left) // 2 # weight of ship

            # Calculate how many days will it take with current weight of the ship
            no_of_days = 1 # Because the first day is already in progress before you load anything
            load = 0
            for w in weights:
                # If the load exceeds the ship weight, load it the next day
                if load + w > mid:
                    no_of_days += 1
                    load = w
                
                else:
                    load += w
            
            # Adjust the capacity
            if no_of_days <= days:
                # If the weight of ship is high such that we are taking less days than given days, we can try reducing the load of ship
                ships_weight = mid
                right = mid
            else:
                left = mid + 1
        
        return ships_weight