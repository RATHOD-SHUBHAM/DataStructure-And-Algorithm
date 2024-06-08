
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1,1]]
        
        
        op = [[1], [1,1]]

        i = 3

        while i <= numRows:

            op_lst = []

            for j in range(1, len(op[-1])):
                cur_sum = op[-1][j-1] + op[-1][j]

                op_lst.append(cur_sum)

            final_lst = [1] + op_lst + [1]

            op.append(final_lst)

            i += 1
        
        return op

