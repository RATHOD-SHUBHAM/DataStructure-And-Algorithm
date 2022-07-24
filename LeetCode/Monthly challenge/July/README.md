# July 2022 LeetCode Challenge.


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
7] 97. Interleaving String

# --------------------------------------------------
8] 1473. Paint House III

# --------------------------------------------------
9] 1696. Jump Game VI

# --------------------------------------------------
10] 746. Min Cost Climbing Stairs

# --------------------------------------------------

12] 473. Matchsticks to Square

sol:
what_to: given an array we got to find out if we can make one square using all the match stick.\
op_req: return true or false

ip: integer array. where array[i] is the length of ith matchstick.

Tc: O(4 ^ n)\
Sc: O(n) # recursice solution

# --------------------------------------------------

13] 102. Binary Tree Level Order Traversal

# --------------------------------------------------

14] 105. Construct Binary Tree from Preorder and Inorder Traversal

# --------------------------------------------------

15] 695. Max Area of Island.


ip: m x n binary matrix grid.\
op: maximum area of an island in grid 
 
 
 sol:
 We have to find the maximum area of island.\
 An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
 
We go to each cell and check if it is a island:\
If it is a iland: \
Check if the adjust 4 neighbor are also neighbor.

Keep track if the area while traversing the neighbors.

Tc: O(m * n), where m and n are the size of matrix\
Sc: O(1).

- Try this along: 200. Number of Islands

# --------------------------------------------------

16] 576. Out of Boundary Paths.

* ip: 
 A m * n grid. \
 Five integers m, n, maxMove, startRow, startColumn. 

* op: 
  Return the number of paths to move the ball out of the grid boundary.

* Tabulation Method:

  Runs Faster. \
  Recursion + Memoization. 

  ** sol:
    From the startRow and startCol we go to all the 4 neighbour and check if we have reached the boundary.\
    We also keep track of the moves while travelling. \
    If we have reached the boundary, then we return 1 else we return zero.\
    We then return the number of ways we can go outside the boundary.

  ** Tc and Sc: O(mnN).\
    m, n refer to the number of rows and columns of the given grid respectively. \
    N refers to the total number of allowed moves.

* Dynamic Programming:
  
  Space Effecient.

  ** Sol:
    For each move, we will find out the next cell in which the ball will located. \
    If it is crossing the boundary we add that to path count

  ** Tc: O(mnN)\
  ** Sc: O(mn)


- Try this along:146. LRU Cache

# --------------------------------------------------

17] 629. K Inverse Pairs Array

# --------------------------------------------------

18] 1074. Number of Submatrices That Sum to Target

# --------------------------------------------------

19] 118. Pascal's Triangle
```
Pascal's Triangle is a embodiment of DP! Use this as an example when explaining DP next time :^).
```
*ip: A interger Number numRow.

*op: first numRow of pascals triangle.

*Sol:\
 Look at the patter.\
 Below Row is sum of above 2 number in a row. 
 So imagin what will happen if you add 0 to front and back.
 Then calculated the sum.

*Tc: O(numRow ^ 2)\
*Sc: O(1) # Since the input and output generally do not count towards the space complexity.

# --------------------------------------------------

20] 792. Number of Matching Subsequences

### Bucketing approach.

ip: String S, array of string word.\ 
op: no of subsequence.

Sol:\
We have to find how many word from array of word [] is matching / or can be formed from String S.

We can use bucketing approach.

First : We form a dictionary of list using ( defaultdict and deque ). --> *bucketing*\
dictionary key = will be starting letter of the word and value = will be list of words
```
{
 'a' : ['a', 'abc' , 'aed'],
 'b' : [ 'bb', 'bad'],
 'e' : ['eod']
}
```

Now we go through every letter in the String S:\
check with the bukcet value.\
if the length of the letter is 1. then we have found one patter. Increase the count of subseq.

If length is not one. We take the remaining letter from the word and add it in aprropriate bucket so as to compare it with string S.

*Tc: O(len(s) + len(word[i])\
*Sc: O(1)

# --------------------------------------------------
