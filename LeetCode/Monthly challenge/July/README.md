# --------------------------------------------------

1] 1710. Maximum Units on a Truck

ip: A 2d Array. Called Boxtypes.
Boxtype contains: 
1. No of boxes.
2. no of units.

And and interger called truck size : which is maximum no of boxes that can be put into truck.

OP: Maximum total no of units that can be put into truck.

Sol:
Sort the boxtype in ascending order based on no of units. 
So now we will have max unit at front and we can keep loading the truck as long as the truck size is reached.size

Since we sort the array we use  O(nlog(n)) time complexity.
ans we dont use any extra space so space complexity is O(1).

# ------------------------------------------------------

2] 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

ip: Cake size : h and w.
horizontal cut: cut from top to current index.
vertical cut: cut from left to current index.

IF the cut is at index 1. then from 0 - 1 is also a cut -- # the edge case

# edge case
From start to fist cut and from bottom to last cut.

op:
max area of piece of cake after the cake is cut into horizontal and vertical cuts.

Sol:
Find the portion of the cake which has the max height and max width.

So find the individual max height and max width.
and then area of cake will be : max height * max width.


Run time = O(nlog(n) + mlog(m))
Space = O(1)

# ----------------------------------------------------

3] 376. Wiggle Subsequence
ip: An integer array.
op: Longest Wiggle subsequence.

Sol:
Check for the peek and Valley across all the points in the given integer array and count the number of peek and valley. 
Return the max count between them

Run Time: O(n)
Space: O(1)

# ------------------------------------------------------

6] 509. Fibonacci Number.

ip: integer number
op: Fibonacci 

Sol:
1] Recursive: 
TC: O(2^n) , SC: O(n)
2] Tabulation:
TC: O(n), SC: O(n)
3] Memoization:
TC: O(n), SC: O(n)
4] Bottom Up approach:
TC: O(n), SC: O(1)
5] Goldern Ratio:
TC: O(log(n)) , SC:O(1)

# -----------------------------------------------------------
