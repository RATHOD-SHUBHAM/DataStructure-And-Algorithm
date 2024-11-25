class Solution:
    def median(self, matrix, R, C):
        #code here
        sorted_array = []
        for row in range(R):
            for col in range(C):
                cur_ele = matrix[row][col]
                sorted_array.append(cur_ele)
                
        sorted_array.sort()
        V = R * C
        return sorted_array[V//2]