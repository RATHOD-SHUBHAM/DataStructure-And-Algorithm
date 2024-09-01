# Simulation

# Tc and Sc: O(m * n) or O(len(original))

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        len_arr = len(original)

        if len_arr != (m * n):
            return []

        arr_2d = [[None for _ in range(n)] for _ in range(m)]
        print(arr_2d)

        row = 0 
        i = 0
        
        while row < m:
            col = 0

            while col < n:
                arr_2d[row][col] = original[i]
                i += 1
                col += 1
            
            row += 1
        
        return arr_2d
    

# ------------------- Math -------------------

'''
1D to 2D array

1D array
x = len(array)

2D array
m = no of row, n = no of col

Row = i // n
Col = i % n
'''

# Tc and Sc: O(m * n) or O(len(original))

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        len_arr = len(original)

        if len_arr != (m * n):
            return []

        arr_2d = [[None for _ in range(n)] for _ in range(m)]
        # print(arr_2d)

        for i in range(len_arr):
            row = i // n
            col = i % n
            arr_2d[row][col] = original[i]
        
        return arr_2d