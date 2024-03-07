class Solution:
    def __init__(self):
        self.result = []

    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)

        # Helper Function ------------------------------------------------
        
        def backTrack(start, cur_str, cur_sum, prev_num):
            # basecase
            if start == n and cur_sum == target:
                print(cur_str)
                val = "".join(cur_str.copy())
                self.result.append(val)
                print("\n")
                return 
            
            for i in range(start, n):
                # operands in the returned expressions should not contain leading zeros.
                if i > start and num[start] == '0':
                    return
                
                cur_sub_str = num[start : i + 1]
                print(cur_sub_str)
                cur_num = int(cur_sub_str)

                # initial condition - where i need to attach the first number
                if not cur_str:
                    backTrack( i+1 , [cur_sub_str], cur_num, cur_num)
                    # print("here")
                else:
                    # add
                    print("a: ",cur_str)
                    backTrack( i+1 , cur_str + ['+'] + [cur_sub_str], cur_sum + cur_num, cur_num)
                    # sub
                    print("s: ",cur_str)
                    backTrack( i+1 , cur_str + ['-'] + [cur_sub_str], cur_sum - cur_num, -cur_num)
                    # mul
                    print("m: ",cur_str)
                    backTrack( i+1 , cur_str + ['*'] + [cur_sub_str], cur_sum - prev_num + cur_num * prev_num, cur_num * prev_num)
            
            return 

            
        
        # Main Function ----------------------------------------

        cur_sum = 0 # keep track of running sum
        cur_str = [] # keep track of running string
        prev_num = 0 # keep track of previous number
        start = 0

        backTrack(start, cur_str, cur_sum, prev_num)
        # print(self.result)
        return self.result