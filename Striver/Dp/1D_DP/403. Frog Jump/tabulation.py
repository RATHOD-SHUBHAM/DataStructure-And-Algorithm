"""
While standing at my current position, If i know my previous jump, I can easily tell if i can reach the end or not.


Eg: 
    If i am standing at stone 7.
    My previous jump was 2.

    From this i can say my next jump is going to be 1,2 or 3.

    So that means i can reach stone 8,9,10 from stone 7.

If 10 is my last stone, then i have reached the end.


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
    
# -------------------- Same Solution --------------------
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        if n < 2:
            return True

        if stones[1] != 1:
            return False

        # stone_mapping = {}
        # for i in range(n):
        #     stone_mapping[stones[i]] = i 
        stone_mapping = set(stones)
        
        
        # for stone in stones:
        #     dp[stone] = set()
        dp = collections.defaultdict(set)
        dp[0].add(0)
        dp[1].add(1)

        for stone in stones:
            if stone == 0:
                continue
            
            for jump in dp[stone]:
                for nxtJump in range(jump-1, jump+2):
                    if nxtJump > 0:
                        nxtPos = stone + nxtJump

                        if nxtPos in stone_mapping:
                            dp[nxtPos].add(nxtJump)
            

        return len(dp[stones[-1]]) > 0