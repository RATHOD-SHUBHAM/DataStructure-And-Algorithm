'''

https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING

Hey guys, super easy solution here, with NO DIRECTION CHECKS!!!
The key here is to realize that the sum of indices on all diagonals are equal.
For example, in

[1,2,3]
[4,5,6]
[7,8,9]

2, 4 are on the same diagonal, and they share the index sum of 1. (2 is matrix[0][1] and 4 is in matrix[1][0]). 3,5,7 are on the same diagonal, and they share the sum of 2. (3 is matrix[0][2], 5 is matrix[1][1], and 7 is matrix [2][0]).

SO, if you can loop through the matrix, store each element by the sum of its indices in a dictionary, you have a collection of all elements on shared diagonals.

The last part is easy, build your answer (a list) by elements on diagonals. To capture the 'zig zag' or 'snake' phenomena of this problem, simply reverse ever other diagonal level. So check if the level is divisible by 2.

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        d={}
		#loop through matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
				#if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
				#If you've already passed over this diagonal, keep adding elements to it!
                    d[i+j].append(matrix[i][j])
		# we're done with the pass, let's build our answer array
        ans= []
		#look at the diagonal and each diagonal's elements
        for entry in d.items():
			#each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
			#snake time, look at the diagonal level
            if entry[0] % 2 == 0:
				#Here we append in reverse order because its an even numbered level/diagonal. 
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans
                
                ```
				
so 2 key facts:
1. Diagonals are defined by the sum of indicies in a 2 dimensional array
2. The snake phenomena can be achieved by reversing every other diagonal level, therefore check if divisible by 2

Let me know if you need further explanation
'''


