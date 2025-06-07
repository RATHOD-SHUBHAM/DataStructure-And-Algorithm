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
"""

class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        n = len(val)
        
        # Create list of (value, weight, ratio, index) tuples
        items = []
        for i in range(n):
            ratio = val[i] / wt[i]  # value-to-weight ratio
            items.append((val[i], wt[i], ratio))
        
        # Sort by ratio in descending order (greedy choice)
        items.sort(key=lambda x: x[2], reverse=True)
        
        max_value = 0.0
        current_weight = 0
        
        for value, weight, ratio in items:
            if current_weight + weight <= capacity:
                # Take the entire item
                max_value += value
                current_weight += weight
            else:
                # Take fraction of the item
                remaining_capacity = capacity - current_weight
                fraction = remaining_capacity / weight
                max_value += value * fraction
                break  # Knapsack is full
        
        return round(max_value, 6)