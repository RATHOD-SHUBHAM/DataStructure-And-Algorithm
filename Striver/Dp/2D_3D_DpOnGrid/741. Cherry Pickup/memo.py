"""
Let's analyze the problem first:
    1. We need to find the maximum cherries we can collect in a round trip.
    2. We start at (0,0), go to (n-1,n-1), and then return to (0,0).
    3. We can only move right or down on the first trip, and left or up on the return trip.
    4. Once we pick a cherry, that cell becomes empty.

The key insight is that we can transform this into a single pass problem by thinking about it differently: we can have two people starting from (0,0) simultaneously and both moving to (n-1,n-1). This is equivalent to our original problem because:

The paths of these two people represent our forward and return paths
If both people land on the same cell, we count the cherry just once


## Why Two Paths from the Same Position?
The original problem asks us to:
    1. Go from (0,0) to (n-1,n-1) picking cherries
    2. Then go back from (n-1,n-1) to (0,0) picking more cherries

Instead of thinking about this as a round trip, we can reimagine it as two people starting from (0,0) simultaneously and both going to (n-1,n-1). This is a clever transformation:
    * Person 1's path represents our forward journey
    * Person 2's path represents our return journey (but in reverse)

If we flip Person 2's path (reversing the direction), it would be equivalent to going from (n-1,n-1) back to (0,0).



## How does c2 = r1 + c1 - r2?
This is based on an important insight: both persons must take the same number of steps at any given time.

If Person 1 is at position (r1,c1), they have taken (r1+c1) steps from the origin.
If Person 2 is at position (r2,c2), they have taken (r2+c2) steps from the origin.

Since both persons move simultaneously (one step at a time), the total steps must be equal:
r1 + c1 = r2 + c2
Therefore:
c2 = r1 + c1 - r2
This allows us to reduce our state from 4D (r1,c1,r2,c2) to 3D (r1,c1,r2), saving memory and computation.


c2 is recalculated in every recursive call, not just once at the beginning of the algorithm.
Each time we make a recursive call with new values for r1, c1, and r2, the function recalculates c2 using the formula. So c2 is not fixed - it's dynamically computed each time based on the current state.

For example:

1. Initial call: dp(0, 0, 0)
    Inside this call, we calculate c2 = 0 + 0 - 0 = 0
    Then we make recursive calls with updated coordinates


2. If we make a recursive call: dp(1, 0, 0) (Person 1 down, Person 2 right)
    Inside this new call, we recalculate c2 = 1 + 0 - 0 = 1
    So Person 2 is now at position (0, 1)


3. For another recursive call: dp(0, 1, 1) (Person 1 right, Person 2 down)
    Inside this call, we recalculate c2 = 0 + 1 - 1 = 0
    So Person 2 is now at position (1, 0)

## Let's trace the key recursive calls and states. we'll focus on the optimal path to make it easier to follow.  
grid = [
    [0, 1, -1],
    [1, 0, -1],
    [1, 1,  1]
]

### Initial Call

    Start with dp(0, 0, 0)
    Calculate c2 = 0 + 0 - 0 = 0
    Both persons are at position (0, 0)
    Cell value is 0, so result = 0
    Need to find the max of four recursive paths

### First Step Options

    Both move down: dp(1, 0, 1)
    Person 1 down, Person 2 right: dp(1, 0, 0)
    Person 1 right, Person 2 down: dp(0, 1, 1)
    Both move right: dp(0, 1, 0)

##Let's follow Option 2 (which turns out to be optimal):
### dp(1, 0, 0)

    Person 1 at (1, 0), Person 2 at (0, 1)
    Calculate c2 = 1 + 0 - 0 = 1
    Cell values: grid[1][0] = 1, grid[0][1] = 1
    Cherry count = 1 + 1 = 2
    Now explore four more options...

For brevity, I'll follow only the optimal path:
### dp(2, 0, 0)

    Person 1 at (2, 0), Person 2 at (0, 2)
    Calculate c2 = 2 + 0 - 0 = 2
    But grid[0][2] = -1 (thorn), so this returns -inf

Let's backtrack and try a different option from dp(1, 0, 0):
### dp(1, 1, 1)

    Person 1 at (1, 1), Person 2 at (1, 1)
    Calculate c2 = 1 + 1 - 1 = 1
    Both are at the same cell with value 0
    Cherry count so far = 2 + 0 = 2
    Now explore four more options...

### dp(2, 1, 2)

    Person 1 at (2, 1), Person 2 at (2, 1)
    Calculate c2 = 2 + 1 - 2 = 1
    Both are at the same cell with value 1
    Cherry count so far = 2 + 1 = 3

### dp(2, 2, 2)

    Person 1 at (2, 2), Person 2 at (2, 2)
    Calculate c2 = 2 + 2 - 2 = 2
    Both are at the same cell (bottom-right) with value 1
    This is our base case since r1=n-1 and c1=n-1
    Final cherry count = 3 + 1 = 4

## Working backward through optimal path:

    Start: (0, 0) + (0, 0) = 0 cherries (empty cell)
    Move: Person 1 down, Person 2 right
        (1, 0) + (0, 1) = 1 + 1 = 2 cherries


    Move: Both to (1, 1) = 0 cherries (empty cell)
    Move: Both to (2, 1) = 1 cherry
    Move: Both to (2, 2) = 1 cherry
    Total = 4 cherries

## Key points from this example:

    Shared cell handling: When both persons are at (1, 1), we only count the cherry once (though in this case it's 0)
    Avoiding thornbushes: The algorithm correctly avoids paths with -1 cells
    Memoization: In practice, many states would be calculated just once and reused
    Optimal path finding: The DP approach finds the maximum cherries by exploring all valid paths

## The optimal solution is 4 cherries, which matches our dry run. 
The path for Person 1 is:
    (0,0) → (1,0) → (1,1) → (2,1) → (2,2)
And for Person 2:
    (0,0) → (0,1) → (1,1) → (2,1) → (2,2)
This represents a forward path of:
    (0,0) → (1,0) → (1,1) → (2,1) → (2,2)
And a return path of:
    (2,2) → (2,1) → (1,1) → (0,1) → (0,0)

"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        memo = {}

        r1 = 0
        c1 = 0
        r2 = 0
        c2 = 0

        total_cherry_picked = self.memoization(r1, c1, r2, c2, n, memo, grid)

        return max(0, total_cherry_picked)

    def memoization(self, r1, c1, r2, c2, n, memo, grid):
        # base case
        if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return -math.inf
        
        # End cell - both will reach end cell at the same time
        if r1 == n - 1 and c1 == n - 1:
            return grid[n-1][n-1]
        
        if (r1, c1, r2, c2) in memo:
            return memo[(r1, c1, r2, c2)]
        
        # Check if both are not in same cell
        if r1 == r2 and c1 == c2:
            # If same cell: Just consider one
            result = grid[r1][c1]
        else:
            result = grid[r1][c1] + grid[r2][c2]

        result += max(
            self.memoization(r1+1, c1, r2+1, c2, n, memo, grid), # Both move down
            self.memoization(r1, c1+1, r2, c2+1, n, memo, grid), # Both move right
            self.memoization(r1+1, c1, r2, c2+1, n, memo, grid), # p1-> down, p2->right
            self.memoization(r1, c1+1, r2+1, c2, n, memo, grid) # p1->right, p2->down
        )

        memo[(r1, c1, r2, c2)] = result
        return memo[(r1, c1, r2, c2)]

# ------------------------- Same Solution -------------------------

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Initialize memoization cache
        # memo[r1][c1][r2] represents maximum cherries that can be picked
        # when person 1 is at (r1,c1) and person 2 is at (r2,c2)
        # Note: c2 = r1 + c1 - r2 since both persons move the same number of steps
        memo = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        
        def dp(r1, c1, r2):
            # Calculate c2 based on r1, c1, r2
            c2 = r1 + c1 - r2
            
            # Out of bounds or thorn cell
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or \
               grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            # Reached the bottom-right corner
            # The equation r1 + c1 = r2 + c2 enforces that when one person reaches the bottom-right corner, the other person must be there too!
            if r1 == n-1 and c1 == n-1:
                return grid[r1][c1]
            
            # Already calculated
            if memo[r1][c1][r2] != -1:
                return memo[r1][c1][r2]
            
            # Current cell(s) cherries
            result = grid[r1][c1]
            if r1 != r2 or c1 != c2:  # If not the same cell
                result += grid[r2][c2]
            
            # Try all possible moves for both persons
            # Person 1: (r1,c1) -> (r1+1,c1) or (r1,c1+1)
            # Person 2: (r2,c2) -> (r2+1,c2) or (r2,c2+1)
            
            # Calculate the best future moves
            result += max(
                dp(r1+1, c1, r2+1),  # Both move down
                dp(r1+1, c1, r2),    # Person 1 down, Person 2 right
                dp(r1, c1+1, r2+1),  # Person 1 right, Person 2 down
                dp(r1, c1+1, r2)     # Both move right
            )
            
            # Cache the result
            memo[r1][c1][r2] = result
            return result
        
        # Start the DP calculation
        result = dp(0, 0, 0)
        # If no valid path exists, return 0
        return max(0, result)
    
# ------------------------- Same Solution different way -------------------------
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        memo = {}

        r1 = 0
        c1 = 0
        r2 = 0

        total_cherry_picked = self.memoization(r1, c1, r2, n, memo, grid)

        return max(0, total_cherry_picked)

    def memoization(self, r1, c1, r2, n, memo, grid):
        # compute c2
        c2 = r1 + c1 - r2

        # base case
        if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return -math.inf
        
        # End cell
        if r1 == n - 1 and c1 == n - 1:
            return grid[n-1][n-1]
        
        if (r1, c1, r2) in memo:
            return memo[(r1, c1, r2)]
        
        result = grid[r1][c1]
        # check if both person are not on same cell
        if r1 != r2 or c1 != c2:
            result += grid[r2][c2]
        

        result += max(
            self.memoization(r1+1, c1, r2, n, memo, grid),
            self.memoization(r1, c1+1, r2, n, memo, grid),
            self.memoization(r1+1, c1, r2+1, n, memo, grid),
            self.memoization(r1, c1+1, r2+1, n, memo, grid)
        )

        memo[(r1, c1, r2)] = result
        return memo[(r1, c1, r2)]
    
# ------------------------- Same Solution with all 4 vaiables -------------------------
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        memo = {}

        r1 = 0
        c1 = 0
        r2 = 0
        c2 = 0

        total_cherry_picked = self.memoization(r1, c1, r2, c2, n, memo, grid)

        return max(0, total_cherry_picked)

    def memoization(self, r1, c1, r2, c2, n, memo, grid):
        # base case
        if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return -math.inf
        
        # End cell
        if r1 == n - 1 and c1 == n - 1:
            return grid[n-1][n-1]
        
        if (r1, c1, r2, c2) in memo:
            return memo[(r1, c1, r2, c2)]
        
        result = grid[r1][c1]
        # check if both person are not on same cell
        if r1 != r2 or c1 != c2:
            result += grid[r2][c2]
        

        result += max(
            self.memoization(r1+1, c1, r2+1, c2, n, memo, grid), # Both move down
            self.memoization(r1, c1+1, r2, c2+1, n, memo, grid), # Both move right
            self.memoization(r1+1, c1, r2, c2+1, n, memo, grid), # p1-> down, p2->right
            self.memoization(r1, c1+1, r2+1, c2, n, memo, grid) # p1->right, p2->down
        )

        memo[(r1, c1, r2, c2)] = result
        return memo[(r1, c1, r2, c2)]