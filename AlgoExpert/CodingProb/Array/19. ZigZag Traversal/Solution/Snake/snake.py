'''
The key here is to realize that the sum of indices on all diagonals are equal.

so 2 key facts:
1. Diagonals are defined by the sum of indicies in a 2 dimensional array
2. The snake phenomena can be achieved by reversing every other diagonal level, therefore check if divisible by 2

'''


class Solution(object):
    def findDiagonalOrder(self, matrix):

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
        
        # print(d)
        
        
        
        # we're done with the pass, let's build our answer array
        ans= []
		#look at the diagonal and each diagonal's elements
        for entry in d.items():
			#each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
            # print(entry)
            # print(entry[0])
            # print(entry[0] % 2)
            
			#snake time, look at the diagonal level # reverse 0, 2,4,6,...
            if entry[0] % 2 == 0:
				#Here we append in reverse order because its an even numbered level/diagonal. 
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
                
            # print(ans)
            # print("\n")
        return ans