class TwoSum:

    def __init__(self):
        self.nums = []
        self.len = 0

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.len += 1
        

    def find(self, value: int) -> bool:
        dic = {}
        
        for i in range(self.len):
            diff = value - self.nums[i]

            if diff in dic:
                return True
            
            dic[self.nums[i]] = i
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)