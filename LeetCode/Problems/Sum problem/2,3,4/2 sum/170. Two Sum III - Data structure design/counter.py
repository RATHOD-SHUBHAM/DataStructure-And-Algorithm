class TwoSum:

    def __init__(self):
        self.dic = {}
        

    def add(self, number: int) -> None:
        # increase the count of the number if it is already present in the dictionary
        if number in self.dic:
            self.dic[number] += 1
        else:
            self.dic[number] = 1

    def find(self, value: int) -> bool:
        
        for a in self.dic.keys():
            diff = value - a
            
            # if they are same the number should have occured more than once , else it should be present in dic
            if a != diff:
                if diff in self.dic:
                    return True
            elif a == diff and self.dic[a] > 1:
                return True
            
        return False
                
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)