class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # convert list to integer
        str_digit = [str(x) for x in digits]
        digit = "".join(str_digit)

        # add one to rightbit
        new_num = int(digit) + 1
        
        # convert integer to list
        res = [int(x) for x in str(new_num)]
        
        return res