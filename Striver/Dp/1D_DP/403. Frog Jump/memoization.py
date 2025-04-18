"""
For memoization, we will use an integer array or map dp, which will initially have all the entries as -1, representing that the answer for these states has not been calculated yet. Then as we proceed, we will store 1 or 0, denoting true or false if the frog can cross the river for these states or not respectively.

We need a way to find out if there is a stone at a particular position or not. This is because when we will find out the next position of the frog, we will check if there is any stone there or not, and then only we will mark the frog's index as the index of stone at that position. This can be done by creating a map mark from the position of stones to their indices.

Why Last Jump Size Matters
Let's say you're at stone position 3. Whether you can reach the end depends not just on your current position, but also on what jumps you're allowed to make next.
Consider two scenarios:

You reached position 3 with a jump of size 1
You reached position 3 with a jump of size 2

These are different states because:

In scenario 1, your next possible jumps are {0, 1, 2} (k-1, k, k+1)
In scenario 2, your next possible jumps are {1, 2, 3} (k-1, k, k+1)

These different jump options might lead to completely different outcomes!
Concrete Example
Let's look at a simple example: [0,1,3,5,7]
Imagine you're at stone 3 (value = 5):

If you got there with a jump of size 2, your next options are {1,2,3}:

Jump 1: Position 6 (no stone)
Jump 2: Position 7 (last stone) ✓
Jump 3: Position 8 (no stone)


If you got there with a jump of size 4, your next options are {3,4,5}:

Jump 3: Position 8 (no stone)
Jump 4: Position 9 (no stone)
Jump 5: Position 10 (no stone)



As you can see, in the first case you can reach the end, but in the second case you can't - even though you're at the same stone!
Why Memoization Needs Both Variables
So if you only memoize based on the stone index, you would incorrectly assume that once you've determined you can reach the end from a certain stone, that's true for all paths through that stone. But as we've seen, that's not the case.
This is a classic example of needing to include the "history" (last jump size) in your state definition because it affects future decisions.
"""
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        # Map every stone to its index
        stones_mapping = {}
        for i in range(n):
            stones_mapping[stones[i]] = i

        if 1 not in stones_mapping:
            return False

        memo = {} # Memoization - stores index, k
        index = 0 # Keep track of current index
        k = 0 # Keep track of what the last jump was.
        
        return self.recursive(index, k, memo, stones_mapping, n, stones)
    
    def recursive(self, index, k, memo, stones_mapping, n, stones):
        # Base case
        if index == n-1:
            # reached the last stone
            return True
        
        if (index, k) in memo:
            # Check if current index and the jump is already present
            # Return if i am able to reach last stone from current index and given jump size k.
            return memo[(index, k)]
        
        # Iterate over the three possibilities {k - 1, k, k + 1}.
        canReach = False
        for nextJump in range(k-1, k+2):
            # Check if nextJump is greater than 0 because the frog cannot jump in the backward direction, and staying at the same index won't change the outcome.
            # Check if, at this next position, there is a stone or not. If there is an entry in dictionary, it implies that the stone is there.
            nextPos = stones[index] + nextJump
            if (nextJump > 0) and (nextPos in stones_mapping):
                # Check if we can reach the last stone from next postion
                next_index = stones_mapping[nextPos]
                canReach_from_nextPos = self.recursive(next_index, nextJump, memo, stones_mapping, n, stones)

                # Check through all the routes
                canReach = canReach or canReach_from_nextPos
        
        memo[(index, k)] = canReach
        return memo[(index, k)]