# Check out equation.png

# Count Subsets with Target Sum

The Mathematical Relationship
Given:

* Array ARR with total sum = S
* We want partitions where S1 - S2 = D and S1 ≥ S2

Key insight: If we partition the array into two subsets with sums S1 and S2, then:

* S1 + S2 = S (total sum)
* S1 - S2 = D (given condition)

Solving these equations:

* Adding: 2×S1 = S + D → S1 = (S + D)/2
* Subtracting: 2×S2 = S - D → S2 = (S - D)/2

The Transformation
The partition problem becomes: "Find the number of ways to select elements that sum to (S + D)/2"
This means:
* Problem (partition with difference) = Problem (count subsets with target sum)
* Where target k = (S + D)/2

Example
Let's say ARR = [1, 1, 2, 3] and D = 1:

* Total sum S = 7
* Target sum k = (7 + 1)/2 = 4
* We need to count subsets that sum to 4
* Valid subsets: {1, 3}, {2, 1, 1}
* Each gives us a valid partition: (4,3) with difference 1

Edge Cases to Handle

1. (S + D) must be even - otherwise no valid partition exists
2. (S + D)/2 ≤ S - the target sum can't exceed total sum
3. D ≤ S - difference can't be larger than total sum

Implementation Strategy
```
def count_partitions_with_diff(arr, d):
    total_sum = sum(arr)
    
    # Edge cases
    if (total_sum + d) % 2 != 0 or d > total_sum:
        return 0
    
    target = (total_sum + d) // 2
    
    # Now solve: count subsets with sum = target
    return count_subsets_with_sum(arr, target)
```

So essentially, the partition problem reduces to the classic "count subsets with target sum" problem, which can be solved using dynamic programming with the recurrence:

* dp[i][sum] = dp[i-1][sum] + dp[i-1][sum-arr[i]]

# ---------------------------------------------------------------------------------- #

# The constraint S1 ≥ S2 is automatically satisfied
## Why S1 ≥ S2 is Automatically Handled
When we solve the equations:

* S1 + S2 = S
* S1 - S2 = D (where D ≥ 0, given in problem)

We get:

* S1 = (S + D)/2
* S2 = (S - D)/2

Key insight: Since D ≥ 0, we have:

* S + D ≥ S - D
* Therefore: (S + D)/2 ≥ (S - D)/2
* Which means: S1 ≥ S2 automatically!

What if D were negative?
If the problem allowed negative D (meaning S2 > S1), then:

* For D = -2, we'd get S1 = (S - 2)/2 and S2 = (S + 2)/2
* Here S2 > S1, violating our constraint

But since the original problem states "S1 ≥ S2" as a constraint AND asks for difference D, it's implicitly assuming D ≥ 0.

Example Verification
Array: [1, 2, 3, 4], D = 2, S = 10

* S1 = (10 + 2)/2 = 6
* S2 = (10 - 2)/2 = 4
* Check: S1 = 6 ≥ S2 = 4 ✓
* Check: S1 - S2 = 6 - 4 = 2 = D ✓

The Mathematical Guarantee
By choosing to find subsets that sum to (S + D)/2, we're automatically ensuring:

1. The remaining elements sum to (S - D)/2
2. Since D ≥ 0, we have (S + D)/2 ≥ (S - D)/2
3. Therefore S1 ≥ S2 is satisfied by construction

In essence: The constraint S1 ≥ S2 is built into our mathematical transformation when D ≥ 0. We don't need additional code to check it - it's guaranteed by the algebra!