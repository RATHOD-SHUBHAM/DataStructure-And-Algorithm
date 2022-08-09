'''
Describe how you could use a single array to implement K stacks.


Time complexities of operations push() and pop() is O(1). The best part of above implementation is, if there is a slot available in stack, then an item can be pushed in any of the stacks, i.e., no wastage of space.

Time Complexity: O(N), as we are using a loop to traverse N times.

Auxiliary Space: O(N), as we are using extra space for stack.

'''