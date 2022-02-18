'''

1131. Maximum of Absolute Value Expression
Medium

Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.

 

Example 1:

Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
Example 2:

Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
 

Constraints:

2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6


'''

'''
https://leetcode.com/problems/maximum-of-absolute-value-expression/discuss/1779482/Python-Sol-or-Properties-of-Absolute-Values

Property of absolute value: f(i, j) = |A[i] – A[j]| + |i – j|
|A-B| can be written in 4 possible ways
         A + B
        -A + B
        -A - B
         A - B
         
|i - j | can be written in 4 ways
        i - j 
        - i + j
        - i - j
        i + j
# since arr1 and arr2 are of equal size
We can combine |A-B| + |i|
i + A + B
i -A + B
i -A - B
i + A - B


'''

# Time and space = O(n)

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        l1, l2, l3, l4 = [] , [], [], []
        
        # abs(A) + abs(B) = max(A+B, A-B, -A+B, -A-B)
        for i in range(len(arr1)):
            l1.append(i + arr1[i] + arr2[i])
            l2.append(i - arr1[i] + arr2[i])
            l3.append(i - arr1[i] - arr2[i])
            l4.append(i + arr1[i] - arr2[i])
            
        print(l1)
        print(l2)
        print(l3)
        print(l4)
        
            
        res = 0
        res = max(res, max(l1) - min(l1))
        print(res)
        res= max(res, max(l2) - min(l2))
        print(res)
        res= max(res, max(l3) - min(l3))
        print(res)
        res= max(res, max(l4) - min(l4))
        print(res)
        
        
        return res