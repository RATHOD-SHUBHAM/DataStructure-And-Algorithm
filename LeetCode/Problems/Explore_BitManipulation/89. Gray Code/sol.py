# https://www.youtube.com/watch?v=k5UYQtKXJGo

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        
        for i in range(n):
            for x in reversed(result):
                # adding one in the front
                add_one = x + (1 << i)
                result += [add_one]
        
        return result