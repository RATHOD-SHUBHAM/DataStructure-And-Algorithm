class Solution:
    def isPossiblePlacement(self, position, m, dist):
        # Greedy Initial Placements
        no_of_balls = 1
        last_position = position[0]

        n = len(position)

        for i in range(1, n):
            cur_placement = position[i]
            cur_dist = cur_placement - last_position

            if cur_dist < dist:
                continue
            else:
                no_of_balls += 1
                last_position = cur_placement
                
                if no_of_balls == m:
                    return True
            
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        n = max(position) - min(position)

        for i in range(1, n + 1):
            dist = i

            if self.isPossiblePlacement(position, m, dist) == False:
                return dist - 1
        
        return -1