class Solution:
    def andOperator(self, x, y):
        """This is AND Operator"""
        return x & y
    
    def orOperator(self, x, y):
        """This is OR Operator"""
        return x | y
    
    def xorOperator(self, x, y):
        """This is XOR operator"""
        return x ^ y
    
    def notOperator(self, n):
        """This is Not Operator"""
        # 1's Compliment, if negative 2s compliment
        return ~n

    def rightShift(self, x, y):
        return x >> y
    
    def leftShift(self, x, y):
        return x << y
    

if __name__ == '__main__':
    obj = Solution()

    print("And Operator")
    print(obj.andOperator(x=13, y=7))
    print("OR Operator")
    print(obj.orOperator(x=13, y=7))
    print("XOR Operator")
    print(obj.xorOperator(x=13, y=7))
    print("NOT Operator")
    print(obj.notOperator(n=5))
    print("Right Shift Operator")
    print(obj.rightShift(x=13, y=2))
    print("Left Shift Operator")
    print(obj.leftShift(x=13, y=2))
