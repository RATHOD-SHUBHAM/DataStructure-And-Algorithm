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

- Same question on leetcode: 295. Find Median from Data Stream

# ----------------------------------
3. Sort K sorted Array.

ip: Non negative integer K and  k - sorted array of integer. \
op: Sorted array. Which sort the array faster than O(nlogn) time.

What is K-sorted?
* A partially sorted array in which all the elements are atmost k position away from their sorted position.

Sol:\
We first create a min heap for first k elements.\
Then we keep removing the minimum value from heap and keep adding the next element from array to the heap. \

Tc: O(nlogk): where n is the no of element in array and log k because we will have atmost k + 1 element in heap.\
Sc: O(k): because we will have atmost k + 1 element in heap and array is being sorted in place so O(1)


- 88. Merge Sorted Array.\
- 23. Merge k Sorted Lists


# ----------------------------------
5. Laptop Rental.
6. Merge Sorted Array.
