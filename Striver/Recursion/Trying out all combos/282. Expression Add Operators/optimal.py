class Solution:
    def __init__(self):
        self.result = []

    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)

        # Helper function ------------------------------
        def backTrack(start, cur_str, cur_sum, prev_num):
            # basecase
            if start == n and cur_sum == target:
                print(cur_str)
                val = "".join(cur_str.copy())
                self.result.append(val)
                return
            
            # if the target is not matched
            if start >= n:
                return
            

            # logic
            for i in range(start , n):
                # Check if there is a leading zero
                if i > start and num[start] == '0':
                    return

                cur_sub_str = num[start : i + 1]
                cur_num = int(cur_sub_str)

                if not cur_str:
                    # if this is the first element
                    backTrack(i + 1, [cur_sub_str], cur_num, cur_num)
                else:
                    # add
                    backTrack(i + 1, cur_str + ['+'] + [cur_sub_str], cur_sum + cur_num, cur_num)

                    # sub
                    backTrack(i + 1, cur_str + ['-'] + [cur_sub_str], cur_sum - cur_num, -cur_num)

                    # mul
                    backTrack(i + 1, cur_str + ['*'] + [cur_sub_str], cur_sum - prev_num + cur_num * prev_num, prev_num * cur_num)
            
            return


        # Main function ------------------------------
        cur_sum = 0
        cur_str = []
        prev_num = 0
        idx = 0
        backTrack(idx, cur_str, cur_sum, prev_num)

        return self.result