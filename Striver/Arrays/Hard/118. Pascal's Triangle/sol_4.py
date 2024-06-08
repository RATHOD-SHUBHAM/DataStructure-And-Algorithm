
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        op = [[1]]

        for i in range(2, numRows+1):

            op_lst = []

            for j in range(1, len(op[-1])):
                cur_sum = op[-1][j-1] + op[-1][j]

                op_lst.append(cur_sum)

            final_lst = [1] + op_lst + [1]

            op.append(final_lst)
        
        return op

