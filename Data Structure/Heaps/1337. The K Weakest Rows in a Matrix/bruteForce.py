'''
Brute Force:
1* Count the number of soldiers for each row --> while keeping track of their index
2* Sort them based on number of soldiers
3* return the index of first K soldiers


Time = O(row(col + logrow))
space = O(row)

'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers_index = []
        
        # step1: O(row.col)
        for row in range(len(mat)):
            no_of_soldiers = 0 #keep track of soldiers for each row
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    break
                no_of_soldiers += 1
            
            # keep track of no_of_soldiers and their index
            soldiers_index.append((no_of_soldiers, row)) 
            
        # print(soldiers_index)
        
        
        # step 2: #O(rowlogrow)
        soldiers_index.sort() # this will sort based on no_of_soldiers and if there is a duplicate it will sort based on index
        
        
        # print(soldiers_index)
        
        #step 3: get the index of first soldiers
        index_of_weakest_soldiers = []
        for i in range(k):
            index_of_weakest_soldiers.append(soldiers_index[i][-1])
            
        
        # print(index_of_weakest_soldiers)
        return index_of_weakest_soldiers     