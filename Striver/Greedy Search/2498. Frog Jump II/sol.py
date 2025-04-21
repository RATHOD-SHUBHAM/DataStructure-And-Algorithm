"""
Key Insight
The crucial insight is about how to minimize the maximum jump. If you can only visit each stone once, you need to plan both the forward and return journeys carefully.

The optimal strategy is to:
* Use alternating stones for the forward journey
* Use the remaining stones for the return journey

This means if you have stones at positions [0,2,5,6,7]:
* Forward path: 0 → 5 → 7 (skipping 2 and 6)
* Return path: 7 → 6 → 2 → 0 (using the stones you skipped)

Why Alternating Stones is Optimal
The alternating pattern isn't just a random approach - it's mathematically optimal because:
* Each stone can only be visited once (including during return). This means we need to split the available stones between our forward and return journeys.
* We want to minimize the maximum jump length. The best way to do this is to distribute the stones as evenly as possible between the two journeys.
* When stones are evenly spaced, the alternating pattern ensures that both forward and return paths have similar maximum jump lengths. If we used a different pattern, one path would have larger jumps than necessary.

Intuition
If you think about it intuitively:
* The longest possible jump in the worst case is between stones that are 2 positions apart in the original array
* By taking alternating stones for each journey, we ensure that no jump is longer than necessary
* Any other distribution might force at least one path to have unnecessarily large jumps

When Does This Matter Most?
The alternating pattern becomes clearly better when stones are unevenly distributed. For example, if there's a large gap between two consecutive stones, the alternating pattern ensures we don't have to jump that entire gap in one go.

Common Logic misunderstanding:
* You don't need to explicitly calculate both forward and reverse jumps
* The problem is about the maximum jump between any two stones that are 2 positions apart in the original array
"""

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        
        if n == 2:
            return stones[1] - stones[0]
        
        max_jump = 0
        
        # Calculate jumps between stones that are 2 positions apart
        for i in range(n - 2):
            current_jump = stones[i+2] - stones[i]
            max_jump = max(max_jump, current_jump)
        
        return max_jump