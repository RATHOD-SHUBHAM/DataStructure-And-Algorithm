
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

# -----------------  Handling the empty array --------------


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        # if numRows == 2:
        #     return [[1], [1,1]]
        
        
        # op = [[1], [1,1]]

        # i = 3

        op = [[1]]

        i = 2

        while i <= numRows:

            op_lst = []

            for j in range(1, len(op[-1])):
                cur_sum = op[-1][j-1] + op[-1][j]

                op_lst.append(cur_sum)

            '''
                Thing to notice here is:
                    Empty list wont get added thus handling on of the edge cases.
            '''
            final_lst = [1] + op_lst + [1]

            op.append(final_lst)

            i += 1
        
        return op

# -----------------  Using FOR loop -------------- 


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        op = [[1]]

        for i in range(2, numRows+1):

            op_lst = []

            for j in range(1, len(op[-1])):
                cur_sum = op[-1][j-1] + op[-1][j]

                op_lst.append(cur_sum)

            final_lst = [1] + op_lst + [1]

            op.append(final_lst)
        
        return op


# -----------------  Using FOR loop Handling edge case -------------- 

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
