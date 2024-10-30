class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)

        left = max(weights) # least capacity of ship we can have to carry the load
        right = sum(weights) # ship with total weight can carry all goods in one day

        min_ship_weight = left

        while left <= right:
            # Current ship capacity
            mid = left + (right - left) // 2

            # Calculating the no of days needed by the ship with current capacity
            no_of_days = 1
            cur_total_weight = 0
            for weight in weights:  
                if cur_total_weight + weight > mid:
                    '''If current boat capacity exceeds'''
                    no_of_days += 1
                    cur_total_weight = weight
                else:
                    cur_total_weight += weight

            if no_of_days > days:
                left = mid + 1
            else:
                min_ship_weight = mid
                right = mid - 1
        
        return min_ship_weight