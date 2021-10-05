class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def __init__(self):
        self.result = 0
    def divisorSum(self, n):
        for i in range(1,n+1):
            if n % i == 0:
                # print(i)
                self.result += i
                # print("The result is : ",self.result)
        return self.result


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)