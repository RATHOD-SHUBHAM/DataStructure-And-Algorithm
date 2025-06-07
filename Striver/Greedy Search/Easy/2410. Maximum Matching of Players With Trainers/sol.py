# Tc : O(mlogm + nlogn)
# Sc: O(m + n)

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        m = len(players)
        n = len(trainers)

        players.sort()
        trainers.sort()

        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            # Check if current trainer capacity match with current player
            if players[p1] <= trainers[p2]:
                p1 += 1
            p2 += 1
        
        return p1