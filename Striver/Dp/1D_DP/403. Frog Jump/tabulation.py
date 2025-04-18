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
        
        # Edge case: First jump must be 1
        if n > 1 and stones[1] != 1:
            return False
            
        # Edge case: Only one stone
        if n == 1:
            return True
            
        # Create a dictionary for O(1) stone position lookups
        stone_positions = set(stones)
        
        # dp[i][j] = True if we can reach stone i with a jump of size j
        dp = {} # Stones, [Jump Size]
        for stone in stones:
            dp[stone] = set()
            
        # Initial position: At stone 0 with jump size 0
        dp[0].add(0)
        
        # Process each stone position
        for stone in stones:
            # Try all jump sizes available at this stone
            for jump in dp[stone]:
                # Skip if this is the initial state (stone 0, jump 0)
                if stone == 0 and jump == 0:
                    # Special case: first jump must be 1
                    next_pos = stone + 1
                    if next_pos in stone_positions:
                        dp[next_pos].add(1)
                    continue
                
                # Try all three possible next jumps: k-1, k, k+1
                for next_jump in [jump-1, jump, jump+1]:
                    if next_jump > 0:  # Can't jump backward or stay in place
                        next_pos = stone + next_jump
                        if next_pos in stone_positions:
                            dp[next_pos].add(next_jump)
            # print(dp)
            # print("\n")
        
        # Check if we can reach the last stone with any jump size
        last_stone = stones[-1]
        return len(dp[last_stone]) > 0
    
# -------------------- Same Solution --------------------

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        
        # Edge case: First jump must be 1
        if n > 1 and stones[1] != 1:
            return False
            
        # Edge case: Only one stone
        if n == 1:
            return True
            
        # Create a dictionary for O(1) stone position lookups
        stone_positions = set(stones)
        
        # dp[i][j] = True if we can reach stone i with a jump of size j
        dp = {} # keeps track of different ways in which this particular stone can be reached, Eg: weather we can take a jump or 1 or 2 or 3 and reach here.
        for stone in stones:
            dp[stone] = set()
            
        # Initial position: At stone 0 with jump size 0
        dp[0].add(0)
        dp[1].add(1)

        # Process each stone position
        for stone in stones:
            # Skip if this is the initial state (stone 0, jump 0)
            if stone == 0:
                continue
            # Try all jump sizes available at this stone
            for jump in dp[stone]:
                # Try all three possible next jumps: k-1, k, k+1
                for next_jump in [jump-1, jump, jump+1]:
                    if next_jump > 0:  # Can't jump backward or stay in place
                        next_pos = stone + next_jump
                        if next_pos in stone_positions:
                            dp[next_pos].add(next_jump)
            # print(dp)
            # print("\n")
        
        # Check if we can reach the last stone with any jump size
        last_stone = stones[-1]
        return len(dp[last_stone]) > 0