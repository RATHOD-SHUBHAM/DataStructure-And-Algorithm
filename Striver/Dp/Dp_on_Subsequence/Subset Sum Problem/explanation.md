Example Input:

Array: [3, 8, 5]
Target sum (k): 11

We want to know if there exists a subset that sums to 11.
Let's trace through the algorithm:

1. Initialize the DP Table
```
dp = [[False for j in range(12)] for i in range(3)]  # (k+1 = 12, n = 3)
```

2. Set First Column to True (Sum = 0)
```
for i in range(3):
    dp[i][0] = True
```
Now our DP table looks like:
    0  1  2  3  4  5  6  7  8  9  10 11
0   T  F  F  F  F  F  F  F  F  F  F  F
1   T  F  F  F  F  F  F  F  F  F  F  F
2   T  F  F  F  F  F  F  F  F  F  F  F

3. Handle First Element
```
if arr[0] <= k:  # 3 <= 11, so True
    dp[0][arr[0]] = True  # dp[0][3] = True
```
Updated DP table:
    0  1  2  3  4  5  6  7  8  9  10 11
0   T  F  F  T  F  F  F  F  F  F  F  F
1   T  F  F  F  F  F  F  F  F  F  F  F
2   T  F  F  F  F  F  F  F  F  F  F  F


4. Main DP Calculation
```
For ind = 1 (element = 8):
    For each target from 1 to 11:

target = 1: 
notTaken = dp[0][1] = False, 
arr[1] > 1, so taken = False
dp[1][1] = False

target = 2: 
notTaken = dp[0][2] = False, 
arr[1] > 2, so taken = False
dp[1][2] = False

target = 3: 
notTaken = dp[0][3] = True, 
arr[1] > 3, so taken = False
dp[1][3] = True

target = 4: 
notTaken = dp[0][4] = False, 
arr[1] > 4, so taken = False
dp[1][4] = False

... (similar for targets 5, 6, 7)

target = 8: 
notTaken = dp[0][8] = False, 
arr[1] = 8 ≤ 8, so taken = dp[0][0] = True
dp[1][8] = True

target = 9: 
notTaken = dp[0][9] = False, 
arr[1] = 8 ≤ 9, so taken = dp[0][1] = False
dp[1][9] = False

target = 10: 
notTaken = dp[0][10] = False, 
arr[1] = 8 ≤ 10, so taken = dp[0][2] = False
dp[1][10] = False

target = 11: notTaken = dp[0][11] = False, 
arr[1] = 8 ≤ 11, so taken = dp[0][3] = True
dp[1][11] = True
```

After processing the second element (index 1), our DP table:
    0  1  2  3  4  5  6  7  8  9  10 11
0   T  F  F  T  F  F  F  F  F  F  F  F
1   T  F  F  T  F  F  F  F  T  F  F  T
2   T  F  F  F  F  F  F  F  F  F  F  F

```
For ind = 2 (element = 5):
    For each target from 1 to 11:

target = 1: 
notTaken = dp[1][1] = False, 
arr[2] > 1, so taken = False
dp[2][1] = False

target = 2: 
notTaken = dp[1][2] = False, 
arr[2] > 2, so taken = False
dp[2][2] = False

target = 3: 
notTaken = dp[1][3] = True, 
arr[2] > 3, so taken = False
dp[2][3] = True

target = 4: 
notTaken = dp[1][4] = False, 
arr[2] > 4, so taken = False
dp[2][4] = False

target = 5: 
notTaken = dp[1][5] = False, 
arr[2] = 5 ≤ 5, so taken = dp[1][0] = True
dp[2][5] = True

target = 6: 
notTaken = dp[1][6] = False, 
arr[2] = 5 ≤ 6, so taken = dp[1][1] = False
dp[2][6] = False

target = 7: 
notTaken = dp[1][7] = False, 
arr[2] = 5 ≤ 7, so taken = dp[1][2] = False
dp[2][7] = False

target = 8: 
notTaken = dp[1][8] = True, 
arr[2] = 5 ≤ 8, so taken = dp[1][3] = True
dp[2][8] = True

target = 9: 
notTaken = dp[1][9] = False, 
arr[2] = 5 ≤ 9, so taken = dp[1][4] = False
dp[2][9] = False

target = 10: 
notTaken = dp[1][10] = False, 
arr[2] = 5 ≤ 10, so taken = dp[1][5] = False
dp[2][10] = False

target = 11: 
notTaken = dp[1][11] = True, 
arr[2] = 5 ≤ 11, so taken = dp[1][6] = False
dp[2][11] = True
```

Final DP table:
    0  1  2  3  4  5  6  7  8  9  10 11
0   T  F  F  T  F  F  F  F  F  F  F  F
1   T  F  F  T  F  F  F  F  T  F  F  T
2   T  F  F  T  F  T  F  F  T  F  F  T


5. Final Result
The answer is dp[n-1][k] = dp[2][11] = True
This means there exists a subset of [3, 8, 5] that sums to 11. Indeed, 3 + 8 = 11.


# ----------------------------------------------------------------------------------------

Array: [3, 7, 2]

Target: 10

DP Table Size: n x (sum+1) = 3 x 11
* Rows: 0, 1, 2 (element indices)
* Cols: 0..10 (target sum)

## Step 1: Initialization
* dp[i][0] = True for all i (sum 0 possible with any prefix, by taking no elements)
* For first element: if arr[0] ≤ sum, set dp[0][arr[0]] = True

Initial table (after base cases):
i/j	0	1	2	3	4	5	6	7	8	9	10
0	T	F	F	T	F	F	F	F	F	F	F
1	T	F	F	F	F	F	F	F	F	F	F
2	T	F	F	F	F	F	F	F	F	F	F

## Step 2: Fill the DP Table
Row 0 (only first element [3])
Already initialized: only 0 and 3 are True.

### Row 1 (elements [3, 7])
For each target sum j:
* Not take: dp[0][j]
* Take: If j ≥ arr[1] (j ≥ 7), then check dp[0][j - 7]

Fill each cell:
* j=0: True (initialized)
* j=1-6: False (cannot get 1-6 from [3] or [3,7])
* j=3: True (inherited from row 0)
* j=7: Can take 7 (j-arr[1]=0), so dp[1][7]=dp[0][0]=True
* j=10: Can we take 7? j-7=3, so dp[0][3]=True ⇒ dp[1][10]=True
* Others: False

i/j	0	1	2	3	4	5	6	7	8	9	10
0	T	F	F	T	F	F	F	F	F	F	F
1	T	F	F	T	F	F	F	T	F	F	T
2	T	F	F	F	F	F	F	F	F	F	F

### Row 2 (elements [3, 7, 2])
* Not take: dp[1][j]
* Take: If j ≥ arr[2] (j ≥ 2), then dp[1][j-2]

Let's compute:
* j=0: True (initialized)
* j=1: False
* j=2: Take 2: dp[1][0]=True ⇒ True
* j=3: Not take: dp[1][3]=True; take: dp[1][1]=False ⇒ True
* j=4: Take 2: dp[1][2]=False ⇒ False
* j=5: Take 2: dp[1][3]=True ⇒ True
* j=6: Take 2: dp[1][4]=False ⇒ False
* j=7: Not take: dp[1][7]=True; take: dp[1][5]=False ⇒ True
* j=8: Take 2: dp[1][6]=False ⇒ False
* j=9: Take 2: dp[1][7]=True ⇒ True
* j=10: Not take: dp[1][10]=True; take: dp[1][8]=False ⇒ True

i/j	0	1	2	3	4	5	6	7	8	9	10
0	T	F	F	T	F	F	F	F	F	F	F
1	T	F	F	T	F	F	F	T	F	F	T
2	T	F	T	T	F	T	F	T	F	T	T

### Step 3: Final Answer
dp[2][10] = True
* So, there exists a subset of [3, 7, 2] that sums to 10.

Explanation of True Values in Last Row:
* 2 = [2]
* 3 = [3]
* 5 = [3,2]
* 7 = [7]
* 9 = [7,2]
* 10 = [3,7]

Full Table (n=3, 0-based):
i/j 0	1	2	3	4	5	6	7	8	9	10
0	T	F	F	T	F	F	F	F	F	F	F
1	T	F	F	T	F	F	F	T	F	F	T
2	T	F	T	T	F	T	F	T	F	T	T

* Each row i = can you make sum j with arr[0]..arr[i]?
* Final answer is dp[2][10]

