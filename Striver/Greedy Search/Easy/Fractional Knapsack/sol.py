"""
# Greedy vs Dynamic Programming: 
 Fractional knapsack uses greedy algorithm (always pick highest ratio), while 0/1 knapsack needs dynamic programming.
 
 * In 0/1 knapsack logic, you either take the entire item or don't take it at all. 
 * In fractional knapsack, you should take items greedily based on their value-to-weight ratio.
 
# Correct approach for Fractional Knapsack:
 The fractional knapsack problem should be solved using a greedy algorithm:

 1. Calculate value-to-weight ratio for each item. ie value for 1 unit weight
 2. Sort items by this ratio in descending order
 First 2 steps will help us pick weight that has higest value, helping us maximize
 
 3. Take items greedily until capacity is full
 4. If an item doesn't fit completely, take a fraction of it

# Real-world analogy
===================
Imagine you're a trader with limited cargo space, and you want to maximize profit:

Gold: $1000 value, 1 kg weight → Ratio = 1000/1 = 1000 per kg
Silver: $500 value, 2 kg weight → Ratio = 500/2 = 250 per kg
Copper: $100 value, 5 kg weight → Ratio = 100/5 = 20 per kg

If you have 3 kg capacity, which should you prioritize? Obviously gold first (highest ratio), then silver, then copper.

# Why this greedy choice is optimal
====================================
Here's the key insight: Since we can take fractions, there's no downside to always picking the most "efficient" item first.
In 0/1 knapsack, we can't take fractions, so sometimes it's better to skip a high-ratio item if it doesn't fit and take multiple smaller items instead. But in fractional knapsack:

If an item has the highest ratio, taking ANY amount of it is better than taking the same weight of any other item
We can always take exactly the amount we need (full item or fraction)

"""

class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        n = len(val)
        
        # Create list of (value, weight, ratio, index) tuples
        items = []
        for i in range(n):
            ratio = val[i] / wt[i]
            items.append((val[i], wt[i], ratio))
        
        # Sort as per value-to-weight ratio -> in descending order (greedy choice)
        items.sort(key = lambda x : x[2], reverse = True)
        
        total_val = 0
        
        for val, wt, _ in items:
            if wt <= capacity:
                # Take the entire item
                total_val += val
                capacity -= wt
            else:
                # Take fraction of the item
                fraction = (val * capacity) / wt
                total_val += fraction
                break # Knapsack is full
        
        return round(total_val, 6)