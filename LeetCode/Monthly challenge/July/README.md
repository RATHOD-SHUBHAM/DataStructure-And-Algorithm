
1] 1710. Maximum Units on a Truck

ip: A 2d Array. Called Boxtypes.
Boxtype contains: 
1. No of boxes.
2. no of units.

And and interger called truck size : which is maximum no of boxes that can be put into truck.

OP: Maximum total no of units that can be put into truck.

Sol:
Sort the boxtype in ascending order based on no of units. \
So now we will have max unit at front and we can keep loading the truck as long as the truck size is reached.size

Since we sort the array we use  O(nlog(n)) time complexity.\
ans we dont use any extra space so space complexity is O(1).

# --------------------------------------------------

2] 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

ip: Cake size : h and w.\
horizontal cut: cut from top to current index.\
vertical cut: cut from left to current index.

IF the cut is at index 1. then from 0 - 1 is also a cut -- # the edge case

# edge case
From start to fist cut and from bottom to last cut.

op:
max area of piece of cake after the cake is cut into horizontal and vertical cuts.

Sol:
Find the portion of the cake which has the max height and max width.

So find the individual max height and max width.\
and then area of cake will be : max height * max width.


Run time = O(nlog(n) + mlog(m))\
Space = O(1)

# --------------------------------------------------

3] 376. Wiggle Subsequence
ip: An integer array.\
op: Longest Wiggle subsequence.

Sol:
Check for the peek and Valley across all the points in the given integer array and count the number of peek and valley. \
Return the max count between them

Run Time: O(n)
Space: O(1)

# --------------------------------------------------
4] 135. Candy

# --------------------------------------------------

5] 128. Longest Consecutive Sequence.
ip: unsorted array
op: longest sequence

sol:
Brute force:
For each number check if the next number is available. Along the way also keep track of the sequence count.\
TC: O(n^3)\
Sc: O(1)

Sort:
Sort the ip array, For each number check if the next number is available. Along the way also keep track of the sequence count.\
Tc: O(nlogn)\
Sc: O(1)

Set:
Create a set. For each number check if the next number is available. Along the way also keep track of the sequence count.\
Tc: O(n)\
Sc: O(n)

# --------------------------------------------------

6] 509. Fibonacci Number.

ip: integer number
op: Fibonacci 

Sol:
1] Recursive: \
TC: O(2^n) , SC: O(n)\
2] Tabulation:\
TC: O(n), SC: O(n)\
3] Memoization:\
TC: O(n), SC: O(n)\
4] Bottom Up approach:\
TC: O(n), SC: O(1)\
5] Goldern Ratio:\
TC: O(log(n)) , SC:O(1)

# --------------------------------------------------
7] 1473. Paint House III

# --------------------------------------------------
8] 1696. Jump Game VI

# --------------------------------------------------
9] 746. Min Cost Climbing Stairs

# --------------------------------------------------

12] 473. Matchsticks to Square

sol:
what_to: given an array we got to find out if we can make one square using all the match stick.\
op_req: return true or false

ip: integer array. where array[i] is the length of ith matchstick.

Tc: O(4 ^ n)\
Sc: O(n) # recursice solution

# --------------------------------------------------
