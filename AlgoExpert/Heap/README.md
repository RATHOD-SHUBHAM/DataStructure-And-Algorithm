# Heaps

1] Min Heap Construction:
ip = Array

Sol:
Build Heap
shift Down
Shift Up
Peek
Remove
Insert

Tc:
Build Heap: O(n)
Remaining: O(log(n))

Sc: O(1)

# ----------------------------------

2] Contineous Median.

Prob statment: any point of time value will be added to array. And we have to return the median of the array.

sol:
Create 2 heap. One that maintain the min stack and one that maintain the max stack and then find the median of the 2 stack by adjusting the length of the stack.

Tc: O(log(n))
Sc: O(n)

Same question on leetcode: 295. Find Median from Data Stream

# ----------------------------------
4. Sort K sorted Array.
5. Laptop Rental.
6. Merge Sorted Array.
