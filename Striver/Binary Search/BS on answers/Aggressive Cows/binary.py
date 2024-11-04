from typing import List

class Solution:
    def isPossiblePlacement(self, stalls, k, dist):
        # Greedy: Initial placements
        no_of_cows = 1
        last_position = stalls[0]

        n = len(stalls)
        for i in range(1, n):
            cur_pos = stalls[i]
            cur_dist =  cur_pos- last_position

            if cur_dist < dist:
                continue
            else:
                last_position = cur_pos
                no_of_cows += 1
            
            # Check if it was possible to place k cows
            if no_of_cows == k:
                return True

        return False
    

    def agressiveCow(self, stalls: List[int], k : int) -> int:

        stalls.sort()
        
        # Max distance will be when first cow is placed in first position and last cow is placed in last position
        right = max(stalls) 
        left = 1

        largest_min_dist = -1

        # Identify if it is possible to place the cows with current distance
        while left <= right:
            mid = left + (right - left) // 2
            
            dist = mid

            if self.isPossiblePlacement(stalls, k , dist) == True:
                largest_min_dist = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return largest_min_dist


if __name__ == '__main__':
    ob = Solution()

    stalls = [1,2,4,8,9] # op = 3
    k = 3

    # stalls = [0,3,4,7,9,10] # op = 3
    # k = 4

    result = ob.agressiveCow(stalls = stalls, k = k)
    print(result)