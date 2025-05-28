# The Mathematical Connection

## The problems boil down to: "Count ways to partition an array into two subsets with a specific difference"

### Q:  Partitions With Given Difference - Dp 18
Subset Difference → Target Sum
In the partition problem:

S1 - S2 = D (given difference)
S1 + S2 = total_sum
Solving: S1 = (D + total_sum) / 2

### Q: 494. Target Sum - Dp 21
Target Sum → Subset Difference
In Target Sum, if we assign + to some numbers and - to others:

arr = +a₁ - a₂ + a₃ - a₄ + a₅
P = (a₁ + a₃ + a₅)
N = (- a₂ - a₄)
Can be rewritten as:
(a₁ + a₃ + a₅) - (a₂ + a₄) = P - N

Let P = sum of numbers with + sign
Let N = sum of numbers with - sign

We want: P - N = target
We also know: P + N = total_sum (sum of all numbers)

Solving these equations:

P = (target + total_sum) / 2
N = (total_sum - target) / 2

So Target Sum becomes: "Count ways to choose a subset that sums to (target + total_sum) / 2"

