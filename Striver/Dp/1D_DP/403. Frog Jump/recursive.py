"""
Just Queston Understanding: https://www.youtube.com/watch?v=3FYCPlIx3YA&t=897s&ab_channel=AlgorithmsMadeEasy

We need a way to find out if there is a stone at a particular position or not. This is because when we will find out the next position of the frog, we will check if there is any stone there or not, and then only we will mark the frog's index as the index of stone at that position. This can be done by creating a map mark from the position of stones to their indices.
"""
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        # Map every stone to its index
        stones_mapping = {} # stone : index
        for i in range(n):
            stones_mapping[stones[i]] = i

        
        index = 0 # Keep track of current index
        k = 0 # Keep track of what the last jump was
        
        return self.recursive(index, k, stones_mapping, n, stones)
    
    def recursive(self, index, k, stones_mapping, n, stones):
        # Base case
        if index == n-1:
            # reached the last stone
            return True
        
        # Iterate over the three possibilities {k - 1, k, k + 1}.
        canReach = False
        for nextJump in range(k-1, k+2):
            # Check if nextJump is greater than 0 because the frog cannot jump in the backward direction, and staying at the same index won't change the outcome.
            # Check if, at this next position, there is a stone or not. If there is an entry in dictionary, it implies that the stone is there.
            nextPos = stones[index] + nextJump
            if (nextJump > 0) and (nextPos in stones_mapping):
                # Check if we can reach the last stone from next postion
                next_index = stones_mapping[nextPos]
                canReach_from_nextPos = self.recursive(next_index, nextJump, stones_mapping, n, stones)

                # Check through all the routes
                canReach = canReach or canReach_from_nextPos
        
        return canReach