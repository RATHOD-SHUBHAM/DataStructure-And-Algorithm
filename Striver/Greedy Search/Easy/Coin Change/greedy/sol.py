#User function Template for python3
"""
Key Difference: Canonical vs Non-Canonical Coin Systems

Indian Currency System (Canonical)
The Indian currency system [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000] is a canonical coin system. This means the greedy algorithm (always pick the largest coin possible) is guaranteed to give the optimal solution.

Arbitrary Coin Systems (Non-Canonical)
In the LeetCode problem, you can have any arbitrary coin denominations like [4, 3, 1] or [3, 4, 1], which are non-canonical. For these systems, greedy doesn't always work.

How will I know this in an interview?
Excellent question! This is a common interview trap. Here's how to handle it professionally:

1. Always Ask Clarifying Questions
When you see a coin change problem, immediately ask:

"Can you clarify the coin denominations? 
- Are we dealing with standard currency (like US coins: 1, 5, 10, 25)?
- Or can the denominations be arbitrary values?"


2. State Your Approach Explicitly
"If this is standard currency, I can use a greedy approach since 
those systems are canonical. But if the denominations are arbitrary, 
I'll need dynamic programming to guarantee the optimal solution."

"""
class Solution:
    def minPartition(self, N):
        # code here
        """
        Safe approach for interviews:
        * Acknowledge both approaches exist
        """
        coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        coins = coins[::-1]
        
        pt = 0
        
        used = []
        
        while N > 0:
            if coins[pt] <= N:
                N -= coins[pt]
                used.append(coins[pt])
            else:
                pt += 1
        
        return used