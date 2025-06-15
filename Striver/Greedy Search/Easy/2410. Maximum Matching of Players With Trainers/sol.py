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

# ---------------------------- Same Solution ----------------------------
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        m = len(players)
        n = len(trainers)
        
        players.sort() 
        trainers.sort()

        i = m - 1
        j = n - 1

        count = 0

        while i >= 0 and j >= 0:
            if players[i] <= trainers[j]:
                count += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        
        return count
